import streamlit as st

data = {
  "社風や企業文化": {
    "年功序列で安定を感じる企業がいい": 2,
    "公平な評価制度を重視したい": 4,
    "社内イベントなどが多く楽しい企業がいい": 3,
    "社員表彰制度などに力を入れている企業がいい": 3,
    "新人サポートが手厚い企業がいい": 3,
    "倫理観が高い企業がいい": 4,
    "外国籍や個性豊かなメンバーの中で刺激を受けられる環境": 3,
    "常にイノベーションを意識している文化がいい": 4,
    "表彰制度が手厚いなど評価制度が充実している企業がいい": 4,
    "上司と部下のコミュニケーションが活発で風通しがいい企業": 5,
    "CSR活動に熱心な企業がいい": 3,
    "地域社会への貢献を重視したい": 3,
    "年功序列ではなく、実力・成果で評価される": 4,
    "中間層が多く、落ち着いたメンバーが多い": 3,
    "若手社員が多く、活気がある": 4
  },
  "事業内容や将来性": {
    "社会的意義がある企業で働きたい": 4,
    "市場シェアが高い企業で活躍したい": 3,
    "技術開発に重きを置いている企業で自分の力を試してみたい": 4,
    "ブランド力が高い企業で最先端の仕事がしたい": 3,
    "将来性や成長性を重視したい": 4,
    "グローバルなビジネスを経験したい": 3,
    "スタートアップ企業で0⇒1を経験したい": 3,
    "新技術やイノベーションを推進する企業で挑戦したい": 4,
    "ユニークな事業に取り組んでいる企業で働きたい": 3,
    "自社開発商品やサービスに強みがある企業で新商品を開発してみたい": 4,
    "DXやITの分野で先駆者となっている企業でスキルを生かしたい": 4,
    "事業規模が大きく業界の影響力が高い企業で働きたい": 3,
    "サステナビリティ経営に取り組んでいる企業がいい": 4,
    "多角経営をしている企業でさまざまな仕事にチャレンジしたい": 3,
    "地元経済の発展に寄与している企業で地元のために働きたい": 3
  },
  "条件面": {
    "希望年収の叶う企業・職種がいい": 4,
    "年々給料が上がっていく会社がいい": 3,
    "能力・成果次第で昇給・昇格していく環境": 4,
    "シフト制・週休二日・完全週休二日がいい": 3,
    "女性も管理職になれる": 4,
    "育児休暇・産休などの休みが取りやすい環境": 4,
    "希望勤務地で働ける": 4,
    "出張はあり・なし": 3,
    "在宅勤務可・不可": 4,
    "残業あり・なし": 3,
    "通勤時間〇時間圏内": 4,
    "研修制度が充実している": 4,
    "資格取得支援がある": 3,
    "時短勤務が可・不可": 4,
    "海外勤務の可能性あり・なし": 3
  },
  "働き方やキャリア": {
    "自己成長できる機会が多い企業で働きたい": 4,
    "早期キャリアアップが期待できる企業で自分のスキルを生かしたい": 4,
    "将来性がある企業でキャリアを築きたい": 4,
    "グローバルな仕事に挑戦できる企業で自分の視野を広げたい": 3,
    "裁量権が大きい企業で仕事をしてみたい": 4,
    "仕事と生活のバランスが取れる企業で長期的に働きたい": 4,
    "挑戦できる環境のある企業で新しいスキルに挑みたい": 4,
    "リーダーシップを育てる企業で将来的にリーダーとして成長したい": 4,
    "異なる分野に挑戦できる企業で多様なキャリアを積みたい": 3,
    "新しい技術に触れられる企業で技術力を高めたい": 4,
    "メンターシップが充実している企業で先輩から学びたい": 4,
    "持続可能な成長を目指す企業で長期的なキャリアを築きたい": 4,
    "性別や年齢を問わず平等にキャリア成長の可能性がある企業で挑戦したい": 4,
    "新卒社員にも昇進の機会がある企業で自分の力を試したい": 3,
    "自分の意志で部署異動ができる企業がいい": 3
  },
  "職種や仕事内容": {
    "最新の技術に触れていたい": 4,
    "研究開発ができる企業がいい": 4,
    "誰かの課題解決に役立つ仕事がいい": 4,
    "自分の専門知識を活かせる職種で働きたい": 4,
    "クリエイティブな仕事で自分の発想力を生かしたい": 4,
    "データ分析や統計に強い職種で論理的思考を発揮したい": 3,
    "プロジェクトでリーダーシップを発揮したい": 4,
    "コンサルティング職で企業やクライアントに提案できる仕事がしたい": 3,
    "マーケティング職でブランド戦略や市場分析に携わりたい": 3,
    "エンジニア職でプログラミングや技術力を生かしたい": 4,
    "研究開発職で新しい技術や製品の開発に関わりたい": 4,
    "企画職で商品やサービスの戦略立案に携わりたい": 3,
    "営業職でクライアントとのコミュニケーション能力を生かしたい": 3,
    "国際業務や海外営業でグローバルな経験を積みたい": 3,
    "人事職で採用や組織開発に携わりたい": 3
  }
}

st.title("カスタムバー可視化例")

# 各カテゴリごとに表示
for category, items in data.items():
    st.subheader(category)
    for label, value in items.items():
        # value は0~5を想定
        # バーの幅を%で計算(0~5 => 0%~100%)
        percentage = (value / 5) * 100
        
        # HTML構築
        html = f"""
        <div style="margin-bottom:20px;">
            <!-- 上部ラベル -->
            <div style="font-weight:bold; margin-bottom:5px; font-size:14px;">
                {label}
            </div>
            <!-- 中段：左0 右5 表示 -->
            <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:5px;">
                <span>0</span>
                <span>5</span>
            </div>
            <!-- 下段：バー本体 -->
            <div style="background-color:#e1e1e1; border-radius:10px; height:20px; width:100%; position:relative;">
                <div style="background-color:#4c9aff; width:{percentage}%; height:100%; border-radius:10px; position:absolute; left:0;">
                </div>
            </div>
        </div>
        """
        
        st.markdown(html, unsafe_allow_html=True)
