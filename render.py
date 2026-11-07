import json
from readme_content import CONTENT
from render_skill_map import load_map, overview, render_details
SKILLS=load_map()
E=json.load(open('data.json'))
IM=json.load(open('images.json'))
try:
  STARS=json.load(open('stars.json'))
except:
  STARS={}
def star_count(e):
  url=e[3]
  if 'github.com/' in url:
    path=url.split('github.com/')[-1].strip('/').split('/')
    if len(path)>=2:
      return STARS.get(f"{path[0]}/{path[1]}", 0)
  return 0
L={'en': {'f': 'README.md',
        'sec': {'gc': 'GameCube',
                'wii': 'Wii',
                'ds': 'Nintendo DS',
                '_3ds': 'Nintendo 3DS',
                'ps1': 'PlayStation',
                'ps2': 'PlayStation 2',
                'saturn': 'Sega Saturn',
                'xbox': 'Xbox / Xbox 360',
                'official': 'Official REA showcases',
                'games': 'Games',
                'pc': 'PC / DOS / PC-98',
                'n64': 'Nintendo 64',
                'md': 'Mega Drive / Genesis',
                'snes': 'Super Famicom / SNES',
                'nes': 'NES / Famicom',
                'gba': 'Game Boy Advance',
                'gb': 'Game Boy',
                'app': 'Apps / Electron / Desktop',
                'protocol': 'Protocols / Hardware',
                'firmware': 'Firmware / Drivers',
                'security': 'Security / Evaluations',
                'tooling': 'Reverse-engineering tools'},
        'sub': {'decomp': 'Decompilation / Recomp',
                'remake': 'Remake / Port',
                'tools': 'Asset extraction & tools'},
        'thx': 'See also / thanks: many REA community entries were cross-checked against '
               '[AIshihzong/awesome-reverse-engineer-anything](https://github.com/AIshihzong/awesome-reverse-engineer-anything).',
        'c': 'Contributing: see [CONTRIBUTING.md](CONTRIBUTING.md). License: [CC0-1.0](LICENSE).'},
 'zh-CN': {'f': 'README.zh-CN.md',
           'sec': {'gc': 'GameCube',
                   'wii': 'Wii',
                   'ds': 'NDS',
                   '_3ds': '3DS',
                   'ps1': 'PS1',
                   'ps2': 'PS2',
                   'saturn': '世嘉土星',
                   'xbox': 'Xbox / Xbox 360',
                   'official': 'REA 官方 Showcase',
                   'games': '游戏',
                   'pc': 'PC / DOS / PC-98',
                   'n64': '任天堂 64',
                   'md': 'MD / Genesis',
                   'snes': 'SFC / SNES',
                   'nes': 'NES / FC',
                   'gba': 'GBA',
                   'gb': 'Game Boy',
                   'app': '应用 / Electron / 桌面',
                   'protocol': '协议 / 硬件',
                   'firmware': '固件 / 驱动',
                   'security': '安全 / 评测',
                   'tooling': '逆向工具'},
           'sub': {'decomp': '反编译 / 重编译', 'remake': '重制 / 移植', 'tools': '资源提取与工具'},
           'thx': '另见 / 致谢：许多 REA 社区条目参考并核对了 '
                  '[AIshihzong/awesome-reverse-engineer-anything](https://github.com/AIshihzong/awesome-reverse-engineer-anything)。',
           'c': '贡献指南见 [CONTRIBUTING.md](CONTRIBUTING.md)。许可：[CC0-1.0](LICENSE)。'},
 'zh-TW': {'f': 'README.zh-TW.md',
           'sec': {'gc': 'GameCube',
                   'wii': 'Wii',
                   'ds': 'NDS',
                   '_3ds': '3DS',
                   'ps1': 'PS1',
                   'ps2': 'PS2',
                   'saturn': 'SEGA Saturn',
                   'xbox': 'Xbox / Xbox 360',
                   'official': 'REA 官方 Showcase',
                   'games': '遊戲',
                   'pc': 'PC / DOS / PC-98',
                   'n64': 'Nintendo 64',
                   'md': 'MD / Genesis',
                   'snes': 'SFC / SNES',
                   'nes': 'NES / FC',
                   'gba': 'GBA',
                   'gb': 'Game Boy',
                   'app': '應用程式 / Electron / 桌面',
                   'protocol': '協定 / 硬體',
                   'firmware': '韌體 / 驅動',
                   'security': '資安 / 評測',
                   'tooling': '逆向工具'},
           'sub': {'decomp': '反編譯 / 重編譯', 'remake': '重製 / 移植', 'tools': '資源擷取與工具'},
           'thx': '另見 / 致謝：許多 REA 社群條目參考並比對了 '
                  '[AIshihzong/awesome-reverse-engineer-anything](https://github.com/AIshihzong/awesome-reverse-engineer-anything)。',
           'c': '貢獻指南見 [CONTRIBUTING.md](CONTRIBUTING.md)。授權：[CC0-1.0](LICENSE)。'},
 'ja': {'f': 'README.ja.md',
        'sec': {'gc': 'ゲームキューブ',
                'wii': 'Wii',
                'ds': 'ニンテンドーDS',
                '_3ds': 'ニンテンドー3DS',
                'ps1': 'PlayStation',
                'ps2': 'PlayStation 2',
                'saturn': 'セガサターン',
                'xbox': 'Xbox / Xbox 360',
                'official': 'REA 公式ショーケース',
                'games': 'ゲーム',
                'pc': 'PC / DOS / PC-98',
                'n64': 'NINTENDO64',
                'md': 'メガドライブ / Genesis',
                'snes': 'スーパーファミコン / SNES',
                'nes': 'ファミコン / NES',
                'gba': 'ゲームボーイアドバンス',
                'gb': 'ゲームボーイ',
                'app': 'アプリ / Electron / デスクトップ',
                'protocol': 'プロトコル / ハードウェア',
                'firmware': 'ファームウェア / ドライバ',
                'security': 'セキュリティ / 評価',
                'tooling': 'リバースエンジニアリングツール'},
        'sub': {'decomp': '逆コンパイル / 再コンパイル', 'remake': 'リメイク / 移植', 'tools': 'アセット抽出・ツール'},
        'thx': '関連リスト／謝辞：REA コミュニティの多くの項目は '
               '[AIshihzong/awesome-reverse-engineer-anything](https://github.com/AIshihzong/awesome-reverse-engineer-anything) '
               'を参照・照合しました。',
        'c': '貢献方法は [CONTRIBUTING.md](CONTRIBUTING.md)、ライセンスは [CC0-1.0](LICENSE)。'},
 'ko': {'f': 'README.ko.md',
        'sec': {'gc': '게임큐브',
                'wii': 'Wii',
                'ds': '닌텐도 DS',
                '_3ds': '닌텐도 3DS',
                'ps1': 'PlayStation',
                'ps2': 'PlayStation 2',
                'saturn': '세가 새턴',
                'xbox': 'Xbox / Xbox 360',
                'official': 'REA 공식 쇼케이스',
                'games': '게임',
                'pc': 'PC / DOS / PC-98',
                'n64': '닌텐도 64',
                'md': '메가 드라이브 / Genesis',
                'snes': '슈퍼 패미컴 / SNES',
                'nes': '패미컴 / NES',
                'gba': '게임보이 어드밴스',
                'gb': '게임보이',
                'app': '앱 / Electron / 데스크톱',
                'protocol': '프로토콜 / 하드웨어',
                'firmware': '펌웨어 / 드라이버',
                'security': '보안 / 평가',
                'tooling': '리버싱 도구'},
        'sub': {'decomp': '디컴파일 / 리컴파일', 'remake': '리메이크 / 포팅', 'tools': '에셋 추출 및 도구'},
        'thx': '참고 / 감사: 많은 REA 커뮤니티 항목은 '
               '[AIshihzong/awesome-reverse-engineer-anything](https://github.com/AIshihzong/awesome-reverse-engineer-anything)을 '
               '참고해 확인했습니다.',
        'c': '기여 방법: [CONTRIBUTING.md](CONTRIBUTING.md). 라이선스: [CC0-1.0](LICENSE).'}}
bar=" · ".join(f"[{n}]({L[k]['f']})" for k,n in [('en','English'),('zh-CN','简体中文'),('zh-TW','繁體中文'),('ja','日本語'),('ko','한국어')])
plats=['nes','snes','md','saturn','gb','gba','n64','gc','wii','ds','3ds','ps1','ps2','xbox','pc']
import re,html
DS=json.load(open('descriptions.json'))
X={
'en':dict(toc="Contents",img="Image",proj="Project",desc="What you get",rea="Uses rea",src="Image source",
  K=dict(readme="Project README",site="Project site",issue="Maintainer post",wiki="Wikipedia (© owner)",shot="Our screenshot",video="Video thumbnail",card="Repo card",none="—"),
  Y=dict(Yes="✅ Yes",No="No",Unverified="❔ Unverified")),
'zh-CN':dict(toc="目录",img="图片",proj="项目",desc="简介",rea="使用 rea",src="图片来源",
  K=dict(readme="项目 README",site="项目网站",issue="维护者发布",wiki="维基百科（© 版权方）",shot="本仓库截图",video="视频封面",card="仓库卡片",none="—"),
  Y=dict(Yes="✅ 是",No="否",Unverified="❔ 待验证")),
'zh-TW':dict(toc="目錄",img="圖片",proj="專案",desc="簡介",rea="使用 rea",src="圖片來源",
  K=dict(readme="專案 README",site="專案網站",issue="維護者貼文",wiki="維基百科（© 版權方）",shot="本儲存庫截圖",video="影片封面",card="儲存庫卡片",none="—"),
  Y=dict(Yes="✅ 是",No="否",Unverified="❔ 待驗證")),
'ja':dict(toc="目次",img="画像",proj="プロジェクト",desc="概要",rea="rea 使用",src="画像の出典",
  K=dict(readme="プロジェクト README",site="公式サイト",issue="メンテナー投稿",wiki="Wikipedia（© 権利者）",shot="当リポジトリの撮影",video="動画サムネイル",card="リポジトリカード",none="—"),
  Y=dict(Yes="✅ はい",No="いいえ",Unverified="❔ 未確認")),
'ko':dict(toc="목차",img="이미지",proj="프로젝트",desc="소개",rea="rea 사용",src="이미지 출처",
  K=dict(readme="프로젝트 README",site="프로젝트 사이트",issue="메인테이너 게시물",wiki="위키백과(© 권리자)",shot="자체 스크린샷",video="동영상 썸네일",card="저장소 카드",none="—"),
  Y=dict(Yes="✅ 예",No="아니요",Unverified="❔ 미확인")),
}
def slug(h,seen):
  s=re.sub(r'[^\w\- ]','',h.strip().lower()).replace(' ','-')
  n=seen.get(s,0);seen[s]=n+1
  return s if n==0 else f'{s}-{n}'
def table(d,x,es,k):
  r=['<table>',f'<tr><th width="170">{x["img"]}</th><th>{x["proj"]}</th><th>{x["desc"]}</th><th>{x["rea"]}</th><th>{x["src"]}</th></tr>']
  for e in es:
    im=IM.get(e[2]);kind=im[0] if im else 'none'
    pic=f'<a href="{e[3]}"><img src="{html.escape(im[1])}" width="160" alt="{html.escape(e[2])}"></a>' if im else '—'
    src=x['K'][kind]
    if kind in('wiki','video','issue') and im and kind!='issue': src=f'<a href="{html.escape(im[1])}">{src}</a>'
    nm=e[2].split('/')[-1] if '/' in e[2] and ' ' not in e[2] else e[2]
    own=f'<br><sub>{e[2].split("/")[0]}</sub>' if '/' in e[2] and ' ' not in e[2] else ''
    r.append(f'<tr><td>{pic}</td><td><a href="{e[3]}"><b>{html.escape(nm)}</b></a>{own}</td><td>{html.escape(DS[e[2]][k])}</td><td>{x["Y"][e[4]]}</td><td><sub>{src}</sub></td></tr>')
  r.append('</table>');return r
for k,d in L.items():
  x=X[k]; text=CONTENT[k]; seen={}; body=[]; toc=[]
  def H(level,title,anchor=None):
    automatic=slug(title,seen)
    if anchor:
      body.extend([f'<a id="{anchor}"></a>', ''])
    toc.append((level,title,anchor or automatic))
    body.extend(['#'*level+' '+title,''])

  H(2,text['start'],'atlas-start')
  body += [f"- **{label}:** {description}" for label,description in text['routes']]
  body += ['',text['search'],'']

  skill_title,skill_lines=overview(k,SKILLS)
  H(2,skill_title,'atlas-skills')
  body += skill_lines

  H(2,text['policy'],'atlas-policy')
  context=dict(sources=len(SKILLS['project_evidence']),date=SKILLS['checked_on'])
  for paragraph in text['policy_lines']:
    body += [paragraph.format(**context),'']

  H(2,d['sec']['games'],'atlas-games')
  for p in plats:
    es=sorted([e for e in E if e[0]==p],key=star_count,reverse=True)
    if not es:continue
    H(3,d['sec'].get(p,d['sec'].get('_'+p)))
    for section in ['decomp','remake','tools']:
      subset=sorted([e for e in es if e[1]==section],key=star_count,reverse=True)
      if subset:
        title=d['sub'][section];slug(title,seen)
        body += [f'#### {title}','']+table(d,x,subset,k)+['']

  for section in ['app','protocol','firmware','security','tooling','official']:
    es=sorted([e for e in E if e[0]==section],key=star_count,reverse=True)
    if es:
      H(2,d['sec'][section],'atlas-'+section)
      body += table(d,x,es,k)+['']

  yes_es=sorted([e for e in E if e[4]=='Yes'],key=star_count,reverse=True)
  if yes_es:
    H(2,text['rea_title'],'atlas-rea')
    body += [text['rea_note'],'','<details>',f"<summary>{text['rea_summary'].format(count=len(yes_es))}</summary>",'']
    body += table(d,x,yes_es,k)+['','</details>','']

  H(2,text['resources'],'atlas-data')
  for paragraph in text['resources_lines']:
    body += [paragraph,'']

  repository_count=sum(bool(re.fullmatch(r'https://github.com/[^/]+/[^/]+/?',e[3])) for e in E)
  stats=text['stats'].format(entries=len(E),repos=repository_count,skills=len(SKILLS['skills']))
  head=[bar,'',f"# {text['title']}",'',text['intro'],'',stats,'','> '+text['notice'],'']
  tl=[f"## {x['toc']}",'']+[("  "*(level-2))+f"- [{title}](#{anchor})" for level,title,anchor in toc]+['']
  output=head+tl+body+['---','',d['thx'],'',d['c'],'']
  open(d['f'],'w',encoding='utf-8').write('\n'.join(output))
render_details(SKILLS,E,DS)
print('ok',len(E))
