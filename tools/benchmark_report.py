#!/usr/bin/env python3
"""Descriptive matched-trial reporting from actual saved contracts and reviews.

Does not run agents or make visual judgments. Review evidence remains an attestation.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import re
import statistics
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'skills/mechanism-figures/scripts'))
from _contract import ValidationError, local_file
from _review import gate


def report(path):
    path=Path(path).resolve()
    if not path.exists() or not path.read_text().strip():
        return {'status':'not_run','trials':0,'notice':'No empirical outcomes are available.'}
    rows=[]; seen=set(); pairs={}
    for n,line in enumerate(path.read_text().splitlines(),1):
        if not line.strip():continue
        row=json.loads(line)
        if not isinstance(row,dict):raise ValidationError('Run must be an object, line '+str(n))
        for key in ['task','agent','seed','condition','input_packet_sha256','budget','contract','reviews','costs']:
            if key not in row:raise ValidationError('Missing run field '+key)
        if row['condition'] not in {'baseline','skill'}:raise ValidationError('Condition must be baseline or skill')
        if not isinstance(row['task'],str) or not isinstance(row['agent'],str) or type(row['seed']) is not int:raise ValidationError('Invalid task/agent/seed identity')
        if not isinstance(row['input_packet_sha256'],str) or not re.fullmatch(r'[a-f0-9]{64}',row['input_packet_sha256']):raise ValidationError('Frozen packet hash is required')
        pair=(row['task'],row['agent'],row['seed']);key=pair+(row['condition'],)
        if key in seen:raise ValidationError('Duplicate trial: '+repr(key))
        seen.add(key)
        if pair in pairs and (pairs[pair]['hash']!=row['input_packet_sha256'] or pairs[pair]['budget']!=row['budget']):
            raise ValidationError('Unmatched packet or total budget: '+repr(pair))
        pairs.setdefault(pair,{'hash':row['input_packet_sha256'],'budget':row['budget'],'conditions':{}})
        if not isinstance(row['reviews'],list) or not row['reviews']:raise ValidationError('Saved review files are required, including failed reviews')
        result=gate(local_file(path.parent,row['contract']),[local_file(path.parent,p) for p in row['reviews']],True)
        scores=[r['weighted_score'] for r in result['reviews'] if r.get('mode')=='independent']
        if not isinstance(row['costs'],dict):raise ValidationError('costs must be an object')
        for k in ['tokens','wall_seconds','tool_calls','compute_seconds']:
            value=row['costs'].get(k)
            if value is not None and (type(value) not in (int,float) or not math.isfinite(value) or value<0):raise ValidationError('Invalid cost '+k)
        observed={'task':row['task'],'agent':row['agent'],'seed':row['seed'],'condition':row['condition'],'status':result['status'],'passed':result['accepted'],'independent_score':min(scores) if scores else None,'costs':row['costs']}
        rows.append(observed);pairs[pair]['conditions'][row['condition']]=observed
    complete=[p for p in pairs.values() if set(p['conditions'])=={'baseline','skill'}]
    differences=[int(p['conditions']['skill']['passed'])-int(p['conditions']['baseline']['passed']) for p in complete]
    summary={}
    for condition in ['baseline','skill']:
        group=[r for r in rows if r['condition']==condition];scores=[r['independent_score'] for r in group if r['independent_score'] is not None]
        summary[condition]={'n':len(group),'passed':sum(r['passed'] for r in group),'pass_rate':sum(r['passed'] for r in group)/len(group) if group else None,'score_mean':statistics.mean(scores) if scores else None,'score_sd':statistics.stdev(scores) if len(scores)>1 else None,'missing_cost_counts':{k:sum(r['costs'].get(k) is None for r in group) for k in ['tokens','wall_seconds','tool_calls','compute_seconds']}}
    return {'status':'descriptive_only','trials':len(rows),'matched_pairs':len(complete),'unpaired_trials':len(rows)-2*len(complete),'paired_pass_rate_difference':statistics.mean(differences) if differences else None,'conditions':summary,'trials_detail':rows,'notice':'Independent review identities and observations are recorded attestations. Descriptive statistics are not a causal efficacy claim; inspect task-level failures and the frozen protocol.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('runs',type=Path);args=parser.parse_args()
    try: print(json.dumps(report(args.runs),indent=2,allow_nan=False))
    except (OSError,ValueError,TypeError,KeyError) as exc:print(json.dumps({'status':'invalid_input','error':str(exc)}));sys.exit(2)
