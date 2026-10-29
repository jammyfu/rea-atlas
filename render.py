import json
E=json.load(open('data.json'))
IM=json.load(open('images.json'))
L={
'en':dict(f='README.md',t="REA Atlas: search what has already been reverse-engineered (evidence-tagged)",tag="Searchable map of reverse-engineering projects. Each entry is tagged **Uses rea: Yes / No / Unverified** for [morluto/rea](https://github.com/morluto/rea). Yes only with public evidence. Use it to check whether someone already rebuilt the app, game, protocol or firmware you are looking at.",
 disc="Unofficial; not affiliated with morluto/rea. No cracks, piracy, ROMs or copyrighted assets are listed or hosted.",
 img="Image: REA showcase illustration from [morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png) (MIT), hot-linked, not re-hosted.",
 sec=dict(gc="GameCube",wii="Wii",ds="Nintendo DS",_3ds="Nintendo 3DS",ps1="PlayStation",ps2="PlayStation 2",saturn="Sega Saturn",xbox="Xbox / Xbox 360",official="Official REA showcases",games="Games",pc="PC / DOS / PC-98",n64="Nintendo 64",md="Mega Drive / Genesis",snes="Super Famicom / SNES",nes="NES / Famicom",gba="Game Boy Advance",gb="Game Boy",app="Apps / Electron / Desktop",protocol="Protocols / Hardware",firmware="Firmware / Drivers",security="Security / Evaluations",tooling="Reverse-engineering tools"),
 sub=dict(decomp="Decompilation / Recomp",remake="Remake / Port",tools="Asset extraction & tools"),u="Uses rea",thx="See also / thanks: many REA community entries were cross-checked against [AIshihzong/awesome-reverse-engineer-anything](https://github.com/AIshihzong/awesome-reverse-engineer-anything).",nes_empty="_No verified entry yet — contributions welcome._",c="Contributing: see [CONTRIBUTING.md](CONTRIBUTING.md). License: [CC0-1.0](LICENSE)."),
'zh-CN':dict(f='README.zh-CN.md',t="REA Atlas：已逆向项目可搜索地图（带证据标记）",tag="可搜索的逆向工程项目地图。每条标注是否使用 [morluto/rea](https://github.com/morluto/rea)：**Uses rea: Yes / No / Unverified**，只有公开证据才标 Yes。用来查「这个应用/游戏/协议/固件有没有人已经重实现过」。",
 disc="非官方，与 morluto/rea 无关联。不收录、不托管破解、盗版、ROM 或版权素材。",img="图片：REA showcase 插图，来自 [morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png)（MIT），直接引用，未转存。",
 sec=dict(gc="GameCube",wii="Wii",ds="NDS",_3ds="3DS",ps1="PS1",ps2="PS2",saturn="世嘉土星",xbox="Xbox / Xbox 360",official="REA 官方 Showcase",games="游戏",pc="PC / DOS / PC-98",n64="任天堂 64",md="MD / Genesis",snes="SFC / SNES",nes="NES / FC",gba="GBA",gb="Game Boy",app="应用 / Electron / 桌面",protocol="协议 / 硬件",firmware="固件 / 驱动",security="安全 / 评测",tooling="逆向工具"),
 sub=dict(decomp="反编译 / 重编译",remake="重制 / 移植",tools="资源提取与工具"),u="Uses rea",thx="另见 / 致谢：许多 REA 社区条目参考并核对了 [AIshihzong/awesome-reverse-engineer-anything](https://github.com/AIshihzong/awesome-reverse-engineer-anything)。",nes_empty="_暂无已验证条目，欢迎补充。_",c="贡献指南见 [CONTRIBUTING.md](CONTRIBUTING.md)。许可：[CC0-1.0](LICENSE)。"),
'zh-TW':dict(f='README.zh-TW.md',t="REA Atlas：逆向工程專案地圖（含 rea 標記）",tag="開源逆向工程專案地圖：遊戲反編譯、靜態重編譯、重新實作、資源擷取工具、通用逆向工具，以及應用程式/協定/韌體逆向。每條標註是否使用 [morluto/rea](https://github.com/morluto/rea)（Reverse Engineer Anything）：**Uses rea: Yes / No / Unverified**，只有在具備公開證據（README、官方 showcase 或儲存庫文件）才標 Yes。",
 disc="非官方，與 morluto/rea 無關聯。不收錄、不託管破解、盜版、ROM 或版權素材。",img="圖片：REA showcase 插圖，來自 [morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png)（MIT），直接連結引用，未另行存放。",
 sec=dict(gc="GameCube",wii="Wii",ds="NDS",_3ds="3DS",ps1="PS1",ps2="PS2",saturn="SEGA Saturn",xbox="Xbox / Xbox 360",official="REA 官方 Showcase",games="遊戲",pc="PC / DOS / PC-98",n64="Nintendo 64",md="MD / Genesis",snes="SFC / SNES",nes="NES / FC",gba="GBA",gb="Game Boy",app="應用程式 / Electron / 桌面",protocol="協定 / 硬體",firmware="韌體 / 驅動",security="資安 / 評測",tooling="逆向工具"),
 sub=dict(decomp="反編譯 / 重編譯",remake="重製 / 移植",tools="資源擷取與工具"),u="Uses rea",thx="另見 / 致謝：許多 REA 社群條目參考並比對了 [AIshihzong/awesome-reverse-engineer-anything](https://github.com/AIshihzong/awesome-reverse-engineer-anything)。",nes_empty="_尚無已驗證條目，歡迎補充。_",c="貢獻指南見 [CONTRIBUTING.md](CONTRIBUTING.md)。授權：[CC0-1.0](LICENSE)。"),
'ja':dict(f='README.ja.md',t="REA Atlas：リバースエンジニアリング・プロジェクトマップ（rea タグ付き）",tag="オープンなリバースエンジニアリング・プロジェクトのマップです。ゲームの逆コンパイル、静的再コンパイル、再実装、アセット抽出ツール、汎用 RE ツール、アプリ／プロトコル／ファームウェア解析を収録し、各項目に [morluto/rea](https://github.com/morluto/rea)（Reverse Engineer Anything）の使用有無 **Uses rea: Yes / No / Unverified** を付けています。Yes は公開された根拠がある場合のみです。",
 disc="非公式であり、morluto/rea とは無関係です。クラック、海賊版、ROM、著作権素材は掲載・配布しません。",img="画像：[morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png) の REA ショーケース図（MIT）を直接参照しています（再ホストなし）。",
 sec=dict(gc="ゲームキューブ",wii="Wii",ds="ニンテンドーDS",_3ds="ニンテンドー3DS",ps1="PlayStation",ps2="PlayStation 2",saturn="セガサターン",xbox="Xbox / Xbox 360",official="REA 公式ショーケース",games="ゲーム",pc="PC / DOS / PC-98",n64="NINTENDO64",md="メガドライブ / Genesis",snes="スーパーファミコン / SNES",nes="ファミコン / NES",gba="ゲームボーイアドバンス",gb="ゲームボーイ",app="アプリ / Electron / デスクトップ",protocol="プロトコル / ハードウェア",firmware="ファームウェア / ドライバ",security="セキュリティ / 評価",tooling="リバースエンジニアリングツール"),
 sub=dict(decomp="逆コンパイル / 再コンパイル",remake="リメイク / 移植",tools="アセット抽出・ツール"),u="Uses rea",thx="関連リスト／謝辞：REA コミュニティの多くの項目は [AIshihzong/awesome-reverse-engineer-anything](https://github.com/AIshihzong/awesome-reverse-engineer-anything) を参照・照合しました。",nes_empty="_検証済みの項目はまだありません。追加歓迎です。_",c="貢献方法は [CONTRIBUTING.md](CONTRIBUTING.md)、ライセンスは [CC0-1.0](LICENSE)。"),
'ko':dict(f='README.ko.md',t="REA Atlas: 리버스 엔지니어링 프로젝트 지도 (rea 태그 포함)",tag="오픈 리버스 엔지니어링 프로젝트 지도입니다. 게임 디컴파일, 정적 리컴파일, 재구현, 에셋 추출 도구, 범용 RE 도구, 앱/프로토콜/펌웨어 분석을 수록하며, 각 항목에 [morluto/rea](https://github.com/morluto/rea)(Reverse Engineer Anything) 사용 여부 **Uses rea: Yes / No / Unverified**를 표시합니다. Yes는 공개 근거가 있을 때만 표시합니다.",
 disc="비공식이며 morluto/rea와 관련이 없습니다. 크랙, 불법 복제, ROM, 저작권 자료는 싣거나 배포하지 않습니다.",img="이미지: [morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png)의 REA 쇼케이스 그림(MIT)을 직접 참조합니다(재호스팅 없음).",
 sec=dict(gc="게임큐브",wii="Wii",ds="닌텐도 DS",_3ds="닌텐도 3DS",ps1="PlayStation",ps2="PlayStation 2",saturn="세가 새턴",xbox="Xbox / Xbox 360",official="REA 공식 쇼케이스",games="게임",pc="PC / DOS / PC-98",n64="닌텐도 64",md="메가 드라이브 / Genesis",snes="슈퍼 패미컴 / SNES",nes="패미컴 / NES",gba="게임보이 어드밴스",gb="게임보이",app="앱 / Electron / 데스크톱",protocol="프로토콜 / 하드웨어",firmware="펌웨어 / 드라이버",security="보안 / 평가",tooling="리버싱 도구"),
 sub=dict(decomp="디컴파일 / 리컴파일",remake="리메이크 / 포팅",tools="에셋 추출 및 도구"),u="Uses rea",thx="참고 / 감사: 많은 REA 커뮤니티 항목은 [AIshihzong/awesome-reverse-engineer-anything](https://github.com/AIshihzong/awesome-reverse-engineer-anything)을 참고해 확인했습니다.",nes_empty="_검증된 항목이 아직 없습니다. 기여를 환영합니다._",c="기여 방법: [CONTRIBUTING.md](CONTRIBUTING.md). 라이선스: [CC0-1.0](LICENSE)."),
}
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
  x=X[k];seen={};body=[];toc=[]
  def H(level,t):
    toc.append((level,t,slug(t,seen)));body.extend(['#'*level+' '+t,''])

  # Top: projects with public evidence of using REA
  yes_es = [e for e in E if e[4]=='Yes']
  if yes_es:
    yes_title = {
      'en': 'Projects that used REA (with evidence)',
      'zh-CN': '已使用 REA 的项目（有公开证据）',
      'zh-TW': '已使用 REA 的專案（有公開證據）',
      'ja': 'REA を使用したプロジェクト（公開証拠あり）',
      'ko': 'REA를 사용한 프로젝트 (공개 증거 있음)'
    }.get(k, 'Projects that used REA (with evidence)')
    H(2, yes_title)
    note = {
      'en': '_These have public evidence (README, official showcase, or repo docs) that they used REA. Search by target (app, game, protocol) before starting your own reverse-engineering._',
      'zh-CN': '_以下项目有公开证据（README、官方 showcase 或仓库文档）表明使用了 REA。开始自己的逆向前，先按目标（应用/游戏/协议）搜一下有没有人已经做过。_',
      'zh-TW': '_以下專案有公開證據（README、官方 showcase 或倉庫文件）表明使用了 REA。開始自己的逆向前，先按目標（應用/遊戲/協議）搜一下有沒有人已經做過。_',
      'ja': '_以下は REA を使用した公開証拠（README、公式 showcase、リポジトリ文書）があるプロジェクトです。自分で逆解析を始める前に、対象（アプリ/ゲーム/プロトコル）で検索してください。_',
      'ko': '_다음은 REA를 사용했다는 공개 증거(README, 공식 쇼케이스, 저장소 문서)가 있는 프로젝트입니다. 직접 역공학을 시작하기 전에 대상(앱/게임/프로토콜)으로 검색해 보세요._'
    }.get(k, '')
    if note:
      body += [note, '']
    body += table(d, x, yes_es, k) + ['']

  H(2,d['sec']['games'])
  for p in plats:
    es=[e for e in E if e[0]==p]
    if not es:continue
    H(3,d['sec'].get(p,d['sec'].get('_'+p)))
    for s in ['decomp','remake','tools']:
      ss=[e for e in es if e[1]==s]
      if ss:
        t=d['sub'][s];slug(t,seen);body+=[f'#### {t}','']+table(d,x,ss,k)+['']
  for s in ['app','protocol','firmware','security','tooling','official']:
    es=[e for e in E if e[0]==s]
    if es:H(2,d['sec'][s]);body+=table(d,x,es,k)+['']
  head=[bar,"",f"# {d['t']}","",d['tag'],"","> "+re.sub(r'(?<=[.。])[^.。]*[.。]$','',d['disc']).strip(),""]
  tl=[f"## {x['toc']}",""]+[("  "*(l-2))+f"- [{t}](#{s})" for l,t,s in toc]+[""]
  slug(x['toc'],seen)
  o=head+tl+body+["---","",d['thx'],"",d['c'],""]
  open(d['f'],'w').write("\n".join(o))
print('ok',len(E))
