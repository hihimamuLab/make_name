
import PySimpleGUI as sg
from random import choice

NAMES = [
    "佐藤", "鈴木", "高橋", "田中", "渡辺", "伊藤", "山本", "中村", "小林", "加藤", "吉田", "山田", "佐々木", "山口", "松本", "井上", "木村", "林", "清水", "山崎",
    "池田", "阿部", "橋本", "山下", "森", "石川", "中島", "前田", "藤田", "後藤", "小川", "岡田", "村上", "長谷川", "村田", "足立", "西村", "太田", "宮崎", "佐野",
    "高田", "増田", "平野", "大野", "菅原", "久保", "杉山", "松田", "千葉", "岡本", "桜井", "野口", "松村", "木下", "菊地", "秋山", "山内", "西田", "古川", "島田",
    "市川", "水野", "小島", "服部", "中川", "上田", "沢田", "原田", "内田", "酒井", "川口", "笠井", "片岡", "荒川", "小野", "白石", "大塚", "石田", "今井", "堀",
    "望月", "永井", "熊谷", "田口", "高木", "森田", "菊池", "山中", "中沢", "浜田", "岩崎", "岡崎", "川崎", "吉岡", "中西", "平岡", "平田", "横山", "今村", "安藤",
    "田村", "福田", "大西", "田畑", "福島", "新井", "小松", "藤原", "黒田", "青木", "石井", "福山", "島崎", "坂本", "工藤", "松井", "岩本", "堀内", "石原", "菅野",
    "三浦", "宮本", "岡野", "森本", "白井", "齊藤", "樋口", "小池", "福井", "岡", "吉川", "栗原", "大島", "松下", "黒木", "小山", "高尾", "小澤", "山島", "小笠原",
    "平井", "井口", "矢野", "松原", "西川", "上野", "小谷", "梅田", "荒井", "高松", "戸田", "北村", "菱田", "北川", "富田", "宮下", "北島", "小田", "田代", "南",
    "白川", "加藤", "東", "吉原", "亀田", "近藤", "山岸", "安田", "平山", "岩井", "藤川", "宮田", "萩原", "岡村", "渋谷", "桑原", "杉本", "堀田", "野村", "栗田",
    "牧野", "大崎", "丸山", "河野", "岩田", "畑中", "金井", "荒木", "竹内", "小泉", "大谷", "奥山", "久保田", "宮内", "伊東", "川上", "大久保", "柳沢", "広瀬", "須藤",
    "島本", "奥村", "梶原", "白石", "佐久間", "石塚", "小嶋", "米田", "上村", "神田", "藤村", "宮島", "永田", "梶田", "松浦", "松野", "古賀", "片山", "奥田", "河合",
    "寺田", "古田", "大沢", "広田", "村山", "川田", "浅野", "五十嵐", "津田", "岸",    "小川田", "成田", "横田", "坂口", "梨本", "佐久島", "横井", "稲垣", "関根", "石垣",
    "福本", "中原", "小磯", "坂井", "松島", "秋元", "中嶋", "岸本", "市原", "井田", "高山", "松岡", "田辺", "菅", "青山", "横山", "富永", "南部", "永井", "池上",
    "森下", "片岡", "植田", "山川", "水口", "石井", "荒川", "森山", "鎌田", "竹村", "丸田", "根岸", "宮城", "佐野", "尾崎", "島田", "大石", "鈴木", "坂田", "原口",
    "武井", "八木", "川端", "長谷川", "本多", "畑山", "江頭", "奥本", "平川", "辻", "西沢", "山形", "大森", "岡野", "小森", "相沢", "岡崎", "宮嵜", "矢崎", "阿部",
    "八島", "河口", "八幡", "城戸", "中尾", "桜井", "市川", "木下", "吉村", "黒田", "小西", "望月", "大久保", "青井", "原田", "稲田", "中井", "小出", "山西", "宮崎",
    "梅原", "飯塚", "佐藤", "柿崎", "後藤", "荒巻", "中居", "古川", "宮澤", "浅井", "浅田", "河村", "宮沢", "若松", "徳永", "石山", "宮原", "植木", "内海", "松永",
    "野口", "加納", "佐伯", "沢村", "西山", "今井", "福永", "池谷", "三上", "宮前", "菊地", "澤田", "長尾", "町田", "飯田", "笠原", "山川田", "田原", "横田町", "和泉",
    "芝田", "野沢", "丹野", "前川", "高見", "沼田", "鳥居", "菊池", "奥村町", "藤原", "八王子", "早川", "関", "片瀬", "山中", "杉山", "秋山", "島", "根本", "五十嵐町",
    "天野", "江原", "高木", "三木", "古谷", "青木", "木村", "栗原", "松崎", "石田", "米田", "清水", "桜井町", "下田", "鈴木町", "横井",
    "中井町", "三浦", "藤島", "下山", "川島", "武田", "金田", "片平", "神戸", "篠原",
    "飯島", "岡山", "田所", "宮崎町", "酒井", "高崎", "松下", "田上", "土屋", "安倍",
    "西田", "伊藤", "山根", "田中町", "岩佐", "荒井", "加藤", "渋谷", "望月町", "高橋",
    "今村", "白鳥", "千田", "林田", "鈴鹿", "伊藤町", "石黒", "大久保町", "相馬", "新美",
    "山川上", "中村", "齋藤", "飯沼", "岡部", "平賀", "広瀬", "長尾町", "新村", "宮川",
    "白井", "熊谷", "山科", "菅原", "増井", "福原", "藤井", "岩下", "青山", "宮本",
    "岡野町", "岡部町", "北川", "川越", "北田", "中瀬", "大木", "菅田", "小原", "森脇",
    "武内", "浜口", "尾崎町", "高原", "清田", "船橋", "福山", "中島", "伊賀", "榊原",
    "桜井市", "村瀬", "千葉", "堀内", "松岡", "竹内", "町井", "栗田", "坂口", "金子",
    "三好", "池内", "市田", "伊東", "神田", "小野", "青柳", "井上", "落合", "加納町",
    "宮沢町", "日高", "杉本", "蒲生", "駒井", "藤原町", "小林", "庄司", "清家", "北沢",
    "日野", "小松", "水谷", "中原", "久野", "小嶋"
]

ALPHABET = [
    "テック", "マトリックス", "インパクト", "コスモス", "クオンタム", "ノヴァ", "フュージョン", "スペクトラム",
    "エボリューション", "ベロシティ", "グラビティ", "インフィニティ", "ホライズン", "フュージョン", "イクイノックス",
    "カオス", "イクリプス", "ジェネシス", "レーザー", "ネオン", "ギャラクシー", "ミラージュ", "ネビュラ",
    "タイタン", "オメガ", "サイバー", "ファントム", "ゼニス", "アストラ", "ヘリックス", "ノヴァ",
    "ブレイズ", "ブレード", "ステルス", "ハイパー", "エレクトラ", "ソレス", "アクセル", "チェイス",
    "アストロ", "ボルト", "プロトン", "エレメント", "スープラ", "フュージョン", "エイペックス", "サンダー",
    "フレア", "イグナイト", "ボルテックス", "ブースト", "エアロ", "コズミック", "ボルテックス", "シャドウ",
    "ハイペリオン", "オリオン", "エクソダス", "イグナイト", "ストラトス", "テンペスト", "ビクトリー",
    "ゼファー", "ゼニス", "ホライズン", "ネオン", "スペクトラム", "スーパーノヴァ", "ノヴァ",
    "キセノン", "ユーフォリア", "アポロ", "ラプター", "ブリッツ", "ネビュラ", "コスモ", "イクリプス",
    "インフィニティ", "ジーロット", "アストラル", "レディアンス", "オーロラ", "インフェルノ", "フュージョン",
    "ネクサス", "オムニ", "ポラリス", "リバーブ", "エアロ", "ジェネシス", "ハイパーノヴァ", "ビスタ",
    "ダイナモ", "プラズマ", "グラビトン", "シグマ", "リミックス", "デルタ", "インセプション", "オリジン",
    "フラッシュ", "サイレンス", "プライム", "フリクション", "ヴァイパー", "シンクロニシティ", "プレミアム", "プライマリー", "ヴィジュアル", "プログレッシブ",
    "ファンダメンタル", "エコノミクス", "シンプル", "アナログ", "デジタル",
    "フォトジェニック", "コンセプチュアル", "アカデミック", "リアルタイム", "サステナビリティ",
    "ユートピア", "ダイナミック", "グローバル", "ローカル", "イノベーティブ",
    "クリエイティブ", "オーセンティック", "エキゾチック", "サスペンスフル", "マジェスティック",
    "スタイリッシュ", "エレガント", "サービス", "ファーストクラス", "ブランディング",
    "コミュニケーション", "アイデンティティ", "ビジネス", "フィナンシャル", "デジタル",
    "テクノロジー", "プラットフォーム", "イノベーション", "アドバイザリー", "エグゼクティブ",
    "マネジメント", "リーダーシップ", "カルチャー", "マインドセット", "ビジョン",
    "ミッション", "ストラテジー", "プロセス", "デザイン", "プロトタイプ",
    "ユーザーインターフェース", "ユーザーエクスペリエンス", "フィードバック", "バリデーション", "マーケティング",
    "ブランドポジショニング", "メッセージング", "コンテンツストラテジー", "キャンペーン", "ソーシャルメディア",
    "デジタルストラテジー", "プロダクトマーケティング", "モバイルマーケティング", "アフィリエイトマーケティング", "コンテンツマーケティング",
    "メールマーケティング", "リテンションマーケティング", "カスタマーエクスペリエンス", "カスタマーサポート", "カスタマーサクセス",
    "カスタマーアドボカシー", "リレーションシップマーケティング", "コーポレートコミュニケーション", "パブリックリレーションズ", "インフルエンサーマーケティング",
    "デジタルプロモーション", "エキスパートサービス", "プロフェッショナルサービ"
]

layout = [
    [sg.Button("実行", key="-submit-", size=(50, 3))],
    [sg.Output(size=(50, 20), key="-output-")]
]

window = sg.Window("Name_Maker!", layout, size=(400, 600))

while True:
    event, values = window.read()
    match event:
        case "-submit-":
            window["-output-"].update("")
            print(choice(ALPHABET) + choice(NAMES))
        case sg.WIN_CLOSED:
            break
