#!/usr/bin/env python
"""
Bitties Automated Commit Script
Automatically updates HANDOVER.md and README.md before each commit
Usage: python bitties_commit.py "Your commit message"
"""

import sys
import os
import subprocess
from datetime import datetime
import json

def update_handover(commit_message):
    """Update HANDOVER.md with latest changes"""
    handover_content = f"""# Bitties Project Handover
Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Latest Commit
- **Message:** {commit_message}
- **Time:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Current System Status
"""
    
    # Check if data files exist and add their status
    if os.path.exists('data/fund_summary.json'):
        with open('data/fund_summary.json', 'r', encoding='utf-8') as f:
            summary = json.load(f)
        handover_content += f"""
### Fund Status
- Total BTC Holdings: {summary.get('total_btc_acquired', 'Unknown')} BTC
- Active Members: {summary.get('active_members', 'Unknown')}
- Total Contributions: R{summary.get('total_contributions_zar', 'Unknown'):,.2f}
- Portfolio Value: R{summary.get('portfolio_value_31_july', 'Unknown'):,.2f}
- Last BTC Purchase: {summary.get('last_btc_purchase', 'Unknown')}
"""
    
    # Add file status
    handover_content += """
### Key Files Status
"""
    key_files = [
        ('app/main.py', 'Flask application with routes'),
        ('app/templates/dashboard.html', 'Main dashboard interface'),
        ('app/static/css/styles.css', 'Masters Tournament themed styling'),
        ('data/historical_data.json', 'Complete transaction history'),
        ('data/fund_summary.json', 'Current fund summary'),
        ('create_historical_data.py', 'Historical data import script')
    ]
    
    for file_path, description in key_files:
        if os.path.exists(file_path):
            mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            handover_content += f"- ✅ `{file_path}` - {description} (Modified: {mod_time.strftime('%Y-%m-%d %H:%M')})\n"
        else:
            handover_content += f"- ❌ `{file_path}` - {description} (NOT FOUND)\n"
    
    # Add recent changes section
    if os.path.exists('HANDOVER.md'):
        with open('HANDOVER.md', 'r', encoding='utf-8') as f:
            old_content = f.read()
            if '## Recent Changes Log' in old_content:
                # Extract existing log
                log_start = old_content.find('## Recent Changes Log')
                existing_log = old_content[log_start:]
                # Limit to last 10 entries
                log_lines = existing_log.split('\n')[1:11]
                recent_log = '\n'.join(log_lines)
            else:
                recent_log = ""
    else:
        recent_log = ""
    
    handover_content += f"""
## Recent Changes Log
- [{datetime.now().strftime('%Y-%m-%d %H:%M')}] {commit_message}
{recent_log}

## Next GPT Instructions
1. Check dashboard at http://localhost:5000/dashboard
2. Verify all data displays correctly
3. Run `python create_historical_data.py` if data needs refresh
4. Check HANDOVER.md for latest status
5. All commits should use: `python bitties_commit.py "message"`
"""
    
    with open('HANDOVER.md', 'w', encoding='utf-8') as f:
        f.write(handover_content)
    
    print("✅ HANDOVER.md updated")

def update_readme_progress(commit_message):
    """Append progress update to README.md"""
    
    progress_entry = f"""
### Update: {datetime.now().strftime('%Y-%m-%d %H:%M')}
- {commit_message}
"""
    
    if os.path.exists('README.md'):
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find or create progress section
        if '## Development Progress' not in content:
            # Add new section before Contributing
            if '## Contributing' in content:
                content = content.replace('## Contributing', 
                    '## Development Progress\n\n' + progress_entry + '\n## Contributing')
            else:
                # Just append
                content += '\n## Development Progress\n\n' + progress_entry
        else:
            # Insert after Development Progress header
            insert_pos = content.find('## Development Progress') + len('## Development Progress\n')
            content = content[:insert_pos] + '\n' + progress_entry + content[insert_pos:]
        
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ README.md updated with progress")
    else:
        print("⚠️ README.md not found")

def run_git_commands(commit_message):
    """Execute git add, commit, and push"""
    try:
        # Add all files
        subprocess.run(['git', 'add', '-A'], check=True)
        print("✅ Files staged")
        
        # Commit with message
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        print("✅ Changes committed")
        
        # Push to origin
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        print("✅ Pushed to GitHub")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python bitties_commit.py \"Your commit message\"")
        print("Example: python bitties_commit.py \"Fixed dashboard data connection\"")
        sys.exit(1)
    
    commit_message = ' '.join(sys.argv[1:])
    
    print(f"\n🚀 Bitties Auto-Commit Script")
    print(f"📝 Commit message: {commit_message}")
    print("-" * 50)
    
    # Update documentation
    update_handover(commit_message)
    update_readme_progress(commit_message)
    
    # Run git commands
    if run_git_commands(commit_message):
        print("\n✅ All done! Changes pushed to GitHub with updated documentation.")
    else:
        print("\n❌ Git operations failed. Check error messages above.")

if __name__ == "__main__":
    main()