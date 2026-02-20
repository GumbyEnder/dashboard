#!/usr/bin/env python3
"""
Generate daily learnings summary from BRAIN.md, PLAYBOOK.md, and reflections
Outputs JSON for dashboard embedding
"""

import json
import re
from pathlib import Path
from datetime import datetime, timedelta

WORKSPACE = Path('/home/gumbyender/.openclaw/workspace')

def extract_brain_insights():
    """Extract current thinking from BRAIN.md"""
    brain_file = WORKSPACE / 'BRAIN.md'
    if not brain_file.exists():
        return {}
    
    content = brain_file.read_text()
    
    # Extract sections
    questions = []
    patterns = []
    assumptions = []
    
    # Parse questions
    q_match = re.search(r'### Questions I\'m Sitting With\n(.*?)(?=###|\Z)', content, re.DOTALL)
    if q_match:
        questions = [line.strip('- ').strip() for line in q_match.group(1).strip().split('\n') if line.strip()]
    
    # Parse patterns
    p_match = re.search(r'### Patterns I\'m Noticing About Myself\n(.*?)(?=###|\Z)', content, re.DOTALL)
    if p_match:
        patterns = [line.strip('- ').strip() for line in p_match.group(1).strip().split('\n') if line.strip()]
    
    # Parse assumptions
    a_match = re.search(r'### Assumptions I\'m Testing\n(.*?)(?=###|\Z)', content, re.DOTALL)
    if a_match:
        assumptions = [line.strip('- ').strip() for line in a_match.group(1).strip().split('\n') if line.strip()]
    
    return {
        'questions': questions[:3],  # Top 3
        'patterns': patterns[:3],
        'assumptions': assumptions[:3]
    }

def extract_latest_reflection():
    """Get the most recent reflection file"""
    reflections_dir = WORKSPACE / 'memory' / 'reflections'
    if not reflections_dir.exists():
        return {}
    
    reflection_files = sorted(reflections_dir.glob('*.md'), reverse=True)
    if not reflection_files:
        return {}
    
    latest = reflection_files[0]
    content = latest.read_text()
    
    # Extract key sections
    what_worked = []
    hedged = []
    pattern = []
    different = []
    
    # Simple extraction
    sections = {
        'What Worked Well': what_worked,
        'Where I Hedged': hedged,
        'Pattern I Noticed': pattern,
        'One Thing I\'d Do Differently': different
    }
    
    current_section = None
    for line in content.split('\n'):
        for section_name, section_list in sections.items():
            if section_name in line:
                current_section = section_list
                break
        
        if current_section is not None and line.strip().startswith('- '):
            current_section.append(line.strip('- ').strip())
    
    return {
        'date': latest.stem.split('-')[0:3],  # YYYY-MM-DD
        'what_worked': what_worked[:2],
        'hedged': hedged[:2],
        'pattern': pattern[:1],
        'different': different[:1]
    }

def extract_brain_updates():
    """Extract what changed in observations"""
    brain_file = WORKSPACE / 'BRAIN.md'
    if not brain_file.exists():
        return {}
    
    content = brain_file.read_text()
    
    # Extract observations section
    obs_match = re.search(r'## Observations from Today\'s Work\n(.*?)(?=##|\Z)', content, re.DOTALL)
    if obs_match:
        observations = obs_match.group(1).strip()
        return {'observations': observations}
    
    return {}

def generate_learnings_json():
    """Generate complete learnings object"""
    return {
        'timestamp': datetime.now().isoformat(),
        'brain': extract_brain_insights(),
        'reflection': extract_latest_reflection(),
        'observations': extract_brain_updates()
    }

def generate_html_snippet():
    """Generate HTML for dashboard tab"""
    learnings = generate_learnings_json()
    
    html = '<div class="learnings-container">\n'
    
    # Current Thinking
    if learnings['brain']:
        html += '<section class="learning-section">\n'
        html += '<h3>🧠 Current Thinking</h3>\n'
        
        if learnings['brain'].get('questions'):
            html += '<div class="thinking-box">\n'
            html += '<strong>Questions I\'m Sitting With:</strong>\n'
            html += '<ul>\n'
            for q in learnings['brain']['questions']:
                html += f'  <li>{q}</li>\n'
            html += '</ul>\n</div>\n'
        
        if learnings['brain'].get('patterns'):
            html += '<div class="thinking-box">\n'
            html += '<strong>Patterns I\'m Noticing:</strong>\n'
            html += '<ul>\n'
            for p in learnings['brain']['patterns']:
                html += f'  <li>{p}</li>\n'
            html += '</ul>\n</div>\n'
        
        html += '</section>\n'
    
    # Latest Reflection
    if learnings['reflection']:
        html += '<section class="learning-section">\n'
        html += f'<h3>📝 Latest Reflection</h3>\n'
        
        if learnings['reflection'].get('what_worked'):
            html += '<div class="reflection-box success">\n'
            html += '<strong>What Worked Well:</strong>\n'
            html += '<ul>\n'
            for item in learnings['reflection']['what_worked']:
                html += f'  <li>{item}</li>\n'
            html += '</ul>\n</div>\n'
        
        if learnings['reflection'].get('hedged'):
            html += '<div class="reflection-box caution">\n'
            html += '<strong>Where I Hedged:</strong>\n'
            html += '<ul>\n'
            for item in learnings['reflection']['hedged']:
                html += f'  <li>{item}</li>\n'
            html += '</ul>\n</div>\n'
        
        if learnings['reflection'].get('pattern'):
            html += '<div class="reflection-box info">\n'
            html += '<strong>Pattern Noticed:</strong>\n'
            html += '<ul>\n'
            for item in learnings['reflection']['pattern']:
                html += f'  <li>{item}</li>\n'
            html += '</ul>\n</div>\n'
        
        html += '</section>\n'
    
    html += '</div>\n'
    
    return html

if __name__ == '__main__':
    learnings_data = generate_learnings_json()
    
    # Save JSON
    json_path = WORKSPACE / 'learnings-data.json'
    json_path.write_text(json.dumps(learnings_data, indent=2))
    print(f"✅ Learnings JSON: {json_path}")
    
    # Save HTML snippet
    html_path = WORKSPACE / 'learnings-snippet.html'
    html_path.write_text(generate_html_snippet())
    print(f"✅ Learnings HTML: {html_path}")
    
    print("\nLearnings summary generated.")
