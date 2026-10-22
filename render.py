import json
E=json.load(open('data.json'))
IM=json.load(open('images.json'))
L={
'en':dict(f='README.md',t="REA Atlas",tag="A curated atlas of projects reverse-engineered with [morluto/rea](https://github.com/morluto/rea) (Reverse Engineer Anything), plus comparable decompilation / re-implementation projects. Each entry is marked **Uses rea: Yes / No / Unverified** — Yes only with public evidence (README, official showcase or repo docs).",
 disc="Unofficial; not affiliated with morluto/rea. No cracks, piracy, ROMs or copyrighted assets are listed or hosted. Entry summaries are kept in English in every language edition so the lists stay identical.",
 img="Image: REA showcase illustration from [morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png) (MIT), hot-linked, not re-hosted.",
 sec=dict(official="Official REA showcases",games="Games",pc="PC / DOS / PC-98",n64="Nintendo 64",md="Mega Drive / Genesis",snes="Super Famicom / SNES",nes="NES / Famicom",gba="Game Boy Advance",gb="Game Boy",ps="PlayStation",app="Apps / Electron / Desktop",protocol="Protocols / Hardware",firmware="Firmware / Drivers",security="Security / Evaluations",tooling="Tooling around REA"),
 sub=dict(decomp="Decompilation / Recomp",remake="Remake / Port",tools="Asset extraction & tools"),u="Uses rea",nes_empty="_No verified entry yet — contributions welcome._",c="Contributing: see [CONTRIBUTING.md](CONTRIBUTING.md). License: [CC0-1.0](LICENSE)."),
'zh-CN':dict(f='README.zh-CN.md',t="REA Atlas（REA 图谱）",tag="收录用 [morluto/rea](https://github.com/morluto/rea)（Reverse Engineer Anything）做逆向的项目，以及同类反编译/重实现项目。每条标注 **Uses rea: Yes / No / Unverified**，只有公开证据（README、官方 showcase 或仓库文档）才标 Yes。",
 disc="非官方，与 morluto/rea 无关联。不收录、不托管破解、盗版、ROM 或版权素材。为保证各语言列表一致，条目简介统一保留英文。",img="图片：REA showcase 插图，来自 [morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png)（MIT），直接引用，未转存。",
 sec=dict(official="REA 官方 Showcase",games="游戏",pc="PC / DOS / PC-98",n64="任天堂 64",md="MD / Genesis",snes="SFC / SNES",nes="NES / FC",gba="GBA",gb="Game Boy",ps="PlayStation",app="应用 / Electron / 桌面",protocol="协议 / 硬件",firmware="固件 / 驱动",security="安全 / 评测",tooling="REA 周边工具"),
 sub=dict(decomp="反编译 / 重编译",remake="重制 / 移植",tools="资源提取与工具"),u="Uses rea",nes_empty="_暂无已验证条目，欢迎补充。_",c="贡献指南见 [CONTRIBUTING.md](CONTRIBUTING.md)。许可：[CC0-1.0](LICENSE)。"),
'zh-TW':dict(f='README.zh-TW.md',t="REA Atlas（REA 圖譜）",tag="收錄使用 [morluto/rea](https://github.com/morluto/rea)（Reverse Engineer Anything）進行逆向的專案，以及同類反編譯/重新實作專案。每條標註 **Uses rea: Yes / No / Unverified**，僅有公開證據（README、官方 showcase 或倉庫文件）才標 Yes。",
 disc="非官方，與 morluto/rea 無關聯。不收錄、不託管破解、盜版、ROM 或版權素材。為維持各語言清單一致，條目簡介統一保留英文。",img="圖片：REA showcase 插圖，來自 [morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png)（MIT），直接引用，未轉存。",
 sec=dict(official="REA 官方 Showcase",games="遊戲",pc="PC / DOS / PC-98",n64="任天堂 64",md="MD / Genesis",snes="SFC / SNES",nes="NES / FC",gba="GBA",gb="Game Boy",ps="PlayStation",app="應用程式 / Electron / 桌面",protocol="協定 / 硬體",firmware="韌體 / 驅動",security="資安 / 評測",tooling="REA 周邊工具"),
 sub=dict(decomp="反編譯 / 重編譯",remake="重製 / 移植",tools="資源擷取與工具"),u="Uses rea",nes_empty="_尚無已驗證條目，歡迎補充。_",c="貢獻指南見 [CONTRIBUTING.md](CONTRIBUTING.md)。授權：[CC0-1.0](LICENSE)。"),
'ja':dict(f='README.ja.md',t="REA Atlas",tag="[morluto/rea](https://github.com/morluto/rea)（Reverse Engineer Anything）を使ったリバースエンジニアリング事例と、同種の逆コンパイル／再実装プロジェクトの一覧です。各項目に **Uses rea: Yes / No / Unverified** を付け、公開された根拠（README、公式ショーケース、リポジトリ文書）がある場合のみ Yes とします。",
 disc="非公式であり、morluto/rea とは無関係です。クラック、海賊版、ROM、著作権素材は掲載・配布しません。各言語版で一覧を同一に保つため、項目の説明は英語のままです。",img="画像：[morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png) の REA ショーケース図（MIT）を直接参照しています（再ホストなし）。",
 sec=dict(official="REA 公式ショーケース",games="ゲーム",pc="PC / DOS / PC-98",n64="NINTENDO64",md="メガドライブ / Genesis",snes="スーパーファミコン / SNES",nes="ファミコン / NES",gba="ゲームボーイアドバンス",gb="ゲームボーイ",ps="PlayStation",app="アプリ / Electron / デスクトップ",protocol="プロトコル / ハードウェア",firmware="ファームウェア / ドライバ",security="セキュリティ / 評価",tooling="REA 関連ツール"),
 sub=dict(decomp="逆コンパイル / 再コンパイル",remake="リメイク / 移植",tools="アセット抽出・ツール"),u="Uses rea",nes_empty="_検証済みの項目はまだありません。追加歓迎です。_",c="貢献方法は [CONTRIBUTING.md](CONTRIBUTING.md)、ライセンスは [CC0-1.0](LICENSE)。"),
'ko':dict(f='README.ko.md',t="REA Atlas",tag="[morluto/rea](https://github.com/morluto/rea)(Reverse Engineer Anything)로 리버스 엔지니어링한 프로젝트와 유사한 디컴파일/재구현 프로젝트 목록입니다. 각 항목에 **Uses rea: Yes / No / Unverified**를 표시하며, 공개 근거(README, 공식 쇼케이스, 저장소 문서)가 있을 때만 Yes로 표시합니다.",
 disc="비공식이며 morluto/rea와 관련이 없습니다. 크랙, 불법 복제, ROM, 저작권 자료는 싣거나 배포하지 않습니다. 모든 언어판의 목록을 동일하게 유지하기 위해 항목 설명은 영어로 둡니다.",img="이미지: [morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png)의 REA 쇼케이스 그림(MIT)을 직접 참조합니다(재호스팅 없음).",
 sec=dict(official="REA 공식 쇼케이스",games="게임",pc="PC / DOS / PC-98",n64="닌텐도 64",md="메가 드라이브 / Genesis",snes="슈퍼 패미컴 / SNES",nes="패미컴 / NES",gba="게임보이 어드밴스",gb="게임보이",ps="PlayStation",app="앱 / Electron / 데스크톱",protocol="프로토콜 / 하드웨어",firmware="펌웨어 / 드라이버",security="보안 / 평가",tooling="REA 관련 도구"),
 sub=dict(decomp="디컴파일 / 리컴파일",remake="리메이크 / 포팅",tools="에셋 추출 및 도구"),u="Uses rea",nes_empty="_검증된 항목이 아직 없습니다. 기여를 환영합니다._",c="기여 방법: [CONTRIBUTING.md](CONTRIBUTING.md). 라이선스: [CC0-1.0](LICENSE)."),
}
bar=" · ".join(f"[{n}]({L[k]['f']})" for k,n in [('en','English'),('zh-CN','简体中文'),('zh-TW','繁體中文'),('ja','日本語'),('ko','한국어')])
plats=['pc','n64','md','snes','nes','gba','gb','ps']
for k,d in L.items():
  o=[bar,"",f"# {d['t']}","",d['tag'],"",f"> {d['disc']}","",'<img src="https://raw.githubusercontent.com/morluto/rea/main/docs/assets/rea-showcases.png" alt="REA showcases" width="720" />',"",f"<sub>{d['img']}</sub>",""]
  def line(e):
    t=f"- [{e[2]}]({e[3]}) — **{d['u']}: {e[4]}**. {e[5]}"
    im=IM.get(e[2])
    if not im: return t+"<br><sub>No image.</sub>"
    k,u=im
    cap={'readme':f"Image: {e[2]} ([source]({e[3]}))",'site':f"Site social card from [rea.tools]({e[3]}), not a screenshot",'shot':f"Local headless screenshot of {e[2]}",'card':f"GitHub repo card for [{e[2]}]({e[3]}), not a screenshot"}[k]
    return t+f'<br><img src="{u}" width="240" alt="{e[2]}"><br><sub>{cap}</sub>'

  o+=[f"## {d['sec']['official']}",""]+[line(e) for e in E if e[0]=='official']+["",f"## {d['sec']['games']}",""]
  for p in plats:
    o+=[f"### {d['sec'][p]}",""]
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
