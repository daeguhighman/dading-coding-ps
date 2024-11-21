import os
from github import Github
from datetime import datetime

# GitHub 연결
g = Github(os.environ['GITHUB_TOKEN'])
repo = g.get_repo("daeguhighman/dading-coding-ps")

# 목표 문제 수
goals = {
    "윤동현": 25,
    "정소연": 7,
    "김나리": 18,
    "임경륜": 18,
    "최윤서": 14
}

# progress.md 템플릿
progress_template = """# 📊 Progress Tracking
마지막 업데이트: {}

## 🎯 진행 상황
| 이름 | 진행률 | 완료/목표 |
|------|--------|-----------|
{}

## 📈 상세 진행률
{}
"""

# 진행률에 따른 막대 그래프
def progress_bar(percentage):
    if percentage >= 100:
        return f"🌟 |{'🟩' * 10}| 100%"
    filled = int(percentage / 10)
    remaining = 10 - filled
    return f"🎯 |{'🟦' * filled}{'⬜' * remaining}| {percentage:.1f}%"

# 각 사용자의 파일 수 계산
progress_rows = []
visualization_rows = []
for user, goal in goals.items():
    solved = 0
    for chapter in range(11, 19):
        path = f"Chapter{chapter}/{user}"
        try:
            contents = repo.get_contents(path)
            solved += sum(1 for content in contents if content.path.endswith('.py'))
        except:
            continue
    
    progress = (solved / goal) * 100
    progress_rows.append(f"| {user} | {progress:.1f}% | {solved}/{goal} |")
    visualization_rows.append(f"👤 {user.ljust(4)} {progress_bar(progress)}")

# 현재 시간
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# progress.md 파일 생성
with open('progress.md', 'w', encoding='utf-8') as f:
    f.write(progress_template.format(
        now,
        '\n'.join(progress_rows),
        '\n'.join(visualization_rows)
    ))
