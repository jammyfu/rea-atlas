import json
E=json.load(open('data.json'))
IM=json.load(open('images.json'))
L={
'en':dict(f='README.md',t="REA Atlas: a map of reverse-engineering projects (with rea tags)",tag="A map of open reverse-engineering projects — game decompilations, static recompilations, re-implementations, asset tools, general RE tooling, app/protocol/firmware work — each tagged **Uses rea: Yes / No / Unverified** for [morluto/rea](https://github.com/morluto/rea) (Reverse Engineer Anything). Yes only with public evidence (README, official showcase or repo docs).",
 disc="Unofficial; not affiliated with morluto/rea. No cracks, piracy, ROMs or copyrighted assets are listed or hosted. Entry summaries are kept in English in every language edition so the lists stay identical.",
 img="Image: REA showcase illustration from [morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png) (MIT), hot-linked, not re-hosted.",
 sec=dict(gc="GameCube",wii="Wii",ds="Nintendo DS",_3ds="Nintendo 3DS",ps1="PlayStation",ps2="PlayStation 2",saturn="Sega Saturn",xbox="Xbox / Xbox 360",official="Official REA showcases",games="Games",pc="PC / DOS / PC-98",n64="Nintendo 64",md="Mega Drive / Genesis",snes="Super Famicom / SNES",nes="NES / Famicom",gba="Game Boy Advance",gb="Game Boy",app="Apps / Electron / Desktop",protocol="Protocols / Hardware",firmware="Firmware / Drivers",security="Security / Evaluations",tooling="Tooling around REA"),
 sub=dict(decomp="Decompilation / Recomp",remake="Remake / Port",tools="Asset extraction & tools"),u="Uses rea",nes_empty="_No verified entry yet — contributions welcome._",c="Contributing: see [CONTRIBUTING.md](CONTRIBUTING.md). License: [CC0-1.0](LICENSE)."),
'zh-CN':dict(f='README.zh-CN.md',t="REA Atlas：逆向工程项目地图（含 rea 标记）",tag="开源逆向工程项目地图：游戏反编译、静态重编译、重实现、资源提取工具、通用逆向工具，以及应用/协议/固件逆向。每条标注是否使用 [morluto/rea](https://github.com/morluto/rea)（Reverse Engineer Anything）：**Uses rea: Yes / No / Unverified**，只有公开证据（README、官方 showcase 或仓库文档）才标 Yes。",
 disc="非官方，与 morluto/rea 无关联。不收录、不托管破解、盗版、ROM 或版权素材。为保证各语言列表一致，条目简介统一保留英文。",img="图片：REA showcase 插图，来自 [morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png)（MIT），直接引用，未转存。",
 sec=dict(gc="GameCube",wii="Wii",ds="NDS",_3ds="3DS",ps1="PS1",ps2="PS2",saturn="世嘉土星",xbox="Xbox / Xbox 360",official="REA 官方 Showcase",games="游戏",pc="PC / DOS / PC-98",n64="任天堂 64",md="MD / Genesis",snes="SFC / SNES",nes="NES / FC",gba="GBA",gb="Game Boy",app="应用 / Electron / 桌面",protocol="协议 / 硬件",firmware="固件 / 驱动",security="安全 / 评测",tooling="REA 周边工具"),
 sub=dict(decomp="反编译 / 重编译",remake="重制 / 移植",tools="资源提取与工具"),u="Uses rea",nes_empty="_暂无已验证条目，欢迎补充。_",c="贡献指南见 [CONTRIBUTING.md](CONTRIBUTING.md)。许可：[CC0-1.0](LICENSE)。"),
'zh-TW':dict(f='README.zh-TW.md',t="REA Atlas：逆向工程專案地圖（含 rea 標記）",tag="開源逆向工程專案地圖：遊戲反編譯、靜態重編譯、重新實作、資源擷取工具、通用逆向工具，以及應用程式/協定/韌體逆向。每條標註是否使用 [morluto/rea](https://github.com/morluto/rea)（Reverse Engineer Anything）：**Uses rea: Yes / No / Unverified**，僅有公開證據（README、官方 showcase 或倉庫文件）才標 Yes。",
 disc="非官方，與 morluto/rea 無關聯。不收錄、不託管破解、盜版、ROM 或版權素材。為維持各語言清單一致，條目簡介統一保留英文。",img="圖片：REA showcase 插圖，來自 [morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png)（MIT），直接引用，未轉存。",
 sec=dict(gc="GameCube",wii="Wii",ds="NDS",_3ds="3DS",ps1="PS1",ps2="PS2",saturn="世嘉土星",xbox="Xbox / Xbox 360",official="REA 官方 Showcase",games="遊戲",pc="PC / DOS / PC-98",n64="任天堂 64",md="MD / Genesis",snes="SFC / SNES",nes="NES / FC",gba="GBA",gb="Game Boy",app="應用程式 / Electron / 桌面",protocol="協定 / 硬體",firmware="韌體 / 驅動",security="資安 / 評測",tooling="REA 周邊工具"),
 sub=dict(decomp="反編譯 / 重編譯",remake="重製 / 移植",tools="資源擷取與工具"),u="Uses rea",nes_empty="_尚無已驗證條目，歡迎補充。_",c="貢獻指南見 [CONTRIBUTING.md](CONTRIBUTING.md)。授權：[CC0-1.0](LICENSE)。"),
'ja':dict(f='README.ja.md',t="REA Atlas：リバースエンジニアリング・プロジェクトマップ（rea タグ付き）",tag="オープンなリバースエンジニアリング・プロジェクトのマップです。ゲームの逆コンパイル、静的再コンパイル、再実装、アセット抽出ツール、汎用 RE ツール、アプリ／プロトコル／ファームウェア解析を収録し、各項目に [morluto/rea](https://github.com/morluto/rea)（Reverse Engineer Anything）の使用有無 **Uses rea: Yes / No / Unverified** を付けています。Yes は公開された根拠がある場合のみです。",
 disc="非公式であり、morluto/rea とは無関係です。クラック、海賊版、ROM、著作権素材は掲載・配布しません。各言語版で一覧を同一に保つため、項目の説明は英語のままです。",img="画像：[morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png) の REA ショーケース図（MIT）を直接参照しています（再ホストなし）。",
 sec=dict(gc="ゲームキューブ",wii="Wii",ds="ニンテンドーDS",_3ds="ニンテンドー3DS",ps1="PlayStation",ps2="PlayStation 2",saturn="セガサターン",xbox="Xbox / Xbox 360",official="REA 公式ショーケース",games="ゲーム",pc="PC / DOS / PC-98",n64="NINTENDO64",md="メガドライブ / Genesis",snes="スーパーファミコン / SNES",nes="ファミコン / NES",gba="ゲームボーイアドバンス",gb="ゲームボーイ",app="アプリ / Electron / デスクトップ",protocol="プロトコル / ハードウェア",firmware="ファームウェア / ドライバ",security="セキュリティ / 評価",tooling="REA 関連ツール"),
 sub=dict(decomp="逆コンパイル / 再コンパイル",remake="リメイク / 移植",tools="アセット抽出・ツール"),u="Uses rea",nes_empty="_検証済みの項目はまだありません。追加歓迎です。_",c="貢献方法は [CONTRIBUTING.md](CONTRIBUTING.md)、ライセンスは [CC0-1.0](LICENSE)。"),
'ko':dict(f='README.ko.md',t="REA Atlas: 리버스 엔지니어링 프로젝트 지도 (rea 태그 포함)",tag="오픈 리버스 엔지니어링 프로젝트 지도입니다. 게임 디컴파일, 정적 리컴파일, 재구현, 에셋 추출 도구, 범용 RE 도구, 앱/프로토콜/펌웨어 분석을 수록하며, 각 항목에 [morluto/rea](https://github.com/morluto/rea)(Reverse Engineer Anything) 사용 여부 **Uses rea: Yes / No / Unverified**를 표시합니다. Yes는 공개 근거가 있을 때만 표시합니다.",
 disc="비공식이며 morluto/rea와 관련이 없습니다. 크랙, 불법 복제, ROM, 저작권 자료는 싣거나 배포하지 않습니다. 모든 언어판의 목록을 동일하게 유지하기 위해 항목 설명은 영어로 둡니다.",img="이미지: [morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png)의 REA 쇼케이스 그림(MIT)을 직접 참조합니다(재호스팅 없음).",
 sec=dict(gc="게임큐브",wii="Wii",ds="닌텐도 DS",_3ds="닌텐도 3DS",ps1="PlayStation",ps2="PlayStation 2",saturn="세가 새턴",xbox="Xbox / Xbox 360",official="REA 공식 쇼케이스",games="게임",pc="PC / DOS / PC-98",n64="닌텐도 64",md="메가 드라이브 / Genesis",snes="슈퍼 패미컴 / SNES",nes="패미컴 / NES",gba="게임보이 어드밴스",gb="게임보이",app="앱 / Electron / 데스크톱",protocol="프로토콜 / 하드웨어",firmware="펌웨어 / 드라이버",security="보안 / 평가",tooling="REA 관련 도구"),
 sub=dict(decomp="디컴파일 / 리컴파일",remake="리메이크 / 포팅",tools="에셋 추출 및 도구"),u="Uses rea",nes_empty="_검증된 항목이 아직 없습니다. 기여를 환영합니다._",c="기여 방법: [CONTRIBUTING.md](CONTRIBUTING.md). 라이선스: [CC0-1.0](LICENSE)."),
}
bar=" · ".join(f"[{n}]({L[k]['f']})" for k,n in [('en','English'),('zh-CN','简体中文'),('zh-TW','繁體中文'),('ja','日本語'),('ko','한국어')])
plats=['nes','snes','md','saturn','gb','gba','n64','gc','wii','ds','3ds','ps1','ps2','xbox','pc']
for k,d in L.items():
  o=[bar,"",f"# {d['t']}","",d['tag'],"",f"> {d['disc']}","",'<img src="https://raw.githubusercontent.com/morluto/rea/main/docs/assets/rea-showcases.png" alt="REA showcases" width="720" />',"",f"<sub>{d['img']}</sub>",""]
  def line(e):
    t=f"- [{e[2]}]({e[3]}) — **{d['u']}: {e[4]}**. {e[5]}"
    im=IM.get(e[2])
    if not im: return t+"<br><sub>No image.</sub>"
    k,u=im
    cap={'readme':f"Image: {e[2]} ([source]({e[3]}))",'site':f"Site social card from [rea.tools]({e[3]}), not a screenshot",'shot':f"Our own screenshot: real {e[2].split('/')[-1]} output on /usr/bin/ls (CC0)",'issue':f"Image posted by {e[2]} maintainers in the project's GitHub issues ([repo]({e[3]}))",'wiki':f"Image from the {e[2]} wiki ([repo]({e[3]}))",'card':f"GitHub repo card for [{e[2]}]({e[3]}), not a screenshot"}[k]
    return t+f'<br><img src="{u}" width="240" alt="{e[2]}"><br><sub>{cap}</sub>'

  o+=[f"## {d['sec']['official']}",""]+[line(e) for e in E if e[0]=='official']+["",f"## {d['sec']['games']}",""]
  for p in plats:
    o+=[f"### {d['sec'].get(p,d['sec'].get('_'+p))}",""]
    es=[e for e in E if e[0]==p]
    if not es:o+=[d['nes_empty'],""];continue
    for s in ['decomp','remake','tools']:
      ss=[e for e in es if e[1]==s]
      if ss:o+=[f"#### {d['sub'][s]}",""]+[line(e) for e in ss]+[""]
  for s in ['app','protocol','firmware','security','tooling']:
    o+=[f"## {d['sec'][s]}",""]+[line(e) for e in E if e[0]==s]+[""]
  o+=["---","",d['c'],""]
  open(d['f'],'w').write("\n".join(o))
from collections import Counter
print(Counter(e[0] for e in E),Counter(e[4] for e in E),len(E))
