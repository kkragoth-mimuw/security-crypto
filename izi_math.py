# Piotrek Szulc 347277
import base64
import binascii
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Hash import SHA256

# filter: ip.addr == 35.205.64.152 && udp
messages = [
    '6b366b45784b5a617677474b7462537958484e367a4a786732734b634b4c4f59593955684b74596e504571656b4c74327a46744763624978646272596a76314d6e2b6a3470626355377a49435661346232726154377a734d37525770434151523365784b537649656a41624937445269634266327938457532506f72513445724132696b67366c766a30356a4e744a574c56437168345739672b35685552616e4a74396c4878713530542f64534f486a47616c785363635969526f695957644644586a4630734f4f5434716b57664c6a4659776955353473314a376d743151377a487a645758724670796856396345472f58427066693462566555453671414c30782f4f756d7a61453854474f59387161617267752b714d6c576e474678707a585333786a7a434755315a39516735327464345a643450496b752f2f6c3450523961695778435a4c332f647a2f2b4f62587a2f3252413d3d',
    '6c39514c37775a4c796e53474534537730673278625951333968346f7731302f5a76526d3645526d62436c5a7353426e643755733736655864616a55644e756c617439386b5973677372384d557a767a6772487453583562572f6337663970654c5759626546452b762f754a596a35566d426478447a4c3174722b456867615264336167657963302f61554f34563333376c4c37523136476f342b2f2f67587558596f482b4574384e38427a575279796c6a64493041517a4c495a436a5155595a6e2f37356b754b795971394d7378564b707532415a64414f457752666e326a622f44453767593244524a726b62756a346a4b505a4442394c44337057712b686a6168667a70542b68492b614f41686d6f44623853734b33446856314e6751436d3858336c4359533631545850305370554d5575764b492b5959342b4d6f743645776a30534a56476a5839506b70744f4771694a41773d3d',
    '6d2f38544757593831656542635653765236666f446d775045586d315867626d61684f7370624b6c6e4167553059565949773854625a7a39645a625157726e2b4e64594166563873646b7757554d6e4c4b7131476f38477079746a4e39374371664e2f7370624265382f424a32456849774262725535576f5876313069567a69394557497a5156493545525064764a616d6f68684c6e786b35454258756a534732522b7a6b6d635278514b6a7961583657316e6869565a31465165562f624953772b475352795a47616b76484f4d6275684c7072427039307a76416e546d663369716e39783379764d2b64734a48646f4569663066566f6552382f37424170326d59496b4542524b514c472f623637682f66412f487334617267787669443635415a303232453765734a4a535937516e4a5032564b502f62675950494275527458613657376c755359693571527068594657684936413d3d',
    '6f436f6151385974345670387a795374765549657231506d4c4e56422b4c434e62544c795979446b792b6250386570497a6d6a3536354a6a6459544d514a6858414d794561544d344f646b67546c6569307169662f6754344f627067623462327a466d393077392f4a2b554b546c493736425a6c6d4f6c4730625037545951666564566465554f725179776b3934392b4d664463504e39595267416f68614a776d61426e3757313665515a756d6e3236615245376462336551703463733234304a5a3249395650424d633343612b4b76492b68425972624b6d49736f4a784d34484b69483564347847366458726652546a5643597961722b714a73353572434b39713062667571395343733134494b63677461704f41793364553631446371576a724f76573672706f77377572317a774d6f644d764a79663874436446493672315a6c2b74586b765867544547397135543338312b513d3d',
    '46545a2f484a414b524f7264797635757a2f6f4c39396441553346717666676254766c787a6d63494f445146703033797856714a76524467595075666e342b6877727464526c6436477349586b3676614d4776776d4a3830447a76796768765769663552724a546766476d4336654c494271614f68754a6c6777775467616556456554612f493357636e5363676452592f466777494a5553394663375570306d6f3038706a6d59735976484d386b472b466162617954616947456d65706b6f5a4b4b41443233576f676c4d2f763132336a71483947684e3062326659666a6c796f5067625849737171574d594c7275626375756e36436c70756a616352335a504d795a48767165554d456733357a37714c6a31524c5950467a4547503353424b4e3563666f457a6c786c5535416f53766152644d393258334e4831692b77523464386a576d727a6566506f4c367951704b49624c',
    '42454139715879424662666d4f35723835476f77724e2b755736372b42576566486d342f4c7a796d4f4262764a67772b6e68394242374a32344537336858336f624c6b2f5352706a5061664d4653474467697646537476746f76444f616c686f4a67505066777531464845702b505056384159673162785962537241575571364c434f534f2f754e4a65747a387a4235787372396a51327974744b614a54387063506f56426d70314c656e78586d6279585061444c56727557646b32336f433567356c58544b3575765959777a523173344e713742302b726f2f672b7771745338796f6b773551656c44386b6a7933317251494f576f6549565066503859514a5477434545554e704d6c68684778563376573731394e4b53323655646641744d4a63794349574c574d73457a3078336b4c3556784c784a3543792f6f3430665a53753036344762384b4b48534937677a3465334f52673d3d',
    '4347744530397879495372686d5772375767526e546365466477714b6f42464749593245374b726c5a2f5771526e457653586b6e6861666334447a7a613178424e362f444e4f357641545457457139624b6963657052383845644a67346936306458326772477256534758716276334a4741576248654b365030734c582b5333792f597239317261376130494e4f66674838793445542f6c65384157486d73484144766a70444658566a4b4c55436f62524777677377484e5671395859327050386d52753474516d2b55722f6835796a547a5831614a526c426e6741745a6c5936766969734c613676722f512f4f3558436352775145346d68573657674176626f423856434239534739664c4e33447674397a5633617262474d6c456d3471664b4b436d596c69657250737a6c484b4f36524d634f47797a63494b666e4f5835537166794334714d6d653370584d7161326770432f773d3d',
    '444a5a4c2f6a786a4c4a3363397a72357a353664377139636b6d59584f7272744a4b7a4b71686b6b6c39526c5a745966394e4d4f41353143344372765554716141715a48494d4a36784d48674544307930694a332f324b4b674c507a576755417850647832636e316646717135516538514155565a766f48322b50744a302b6764496d79445270334c626378596167485a414748764c637459627a4c4a7459313147693741754d4d7054792f6f6a753864485a2f613733546d4a71724c574d4e5a596e6d786b79655739432f627a304241714252494f672f6d2b36747355684c57677878347352667169746f59572f6673626f52575477442b78364b52393774516f375a4c464a69554b36476a506d6d3258666443375a6366546932376c735a55725144346f476d5648525566514345322b4959615159564a7979686a39566b64366675574156754d6d452f74794a5a4558336b2f413d3d',
    '454d46544b4a78554f4244595651723452546a556a35637a7263476a315753554a3877515a34646a78374d67687a73516f437a30675a4b6f34426a724e786a797a5a7a4c444a6147694537714463734b6568335257615859373557463064744e4648464442796b5673453972577847766141535073514a425176566c723474304a64346b6654706835676e76655844766b326c736a334f4b614d6935506f433137594362496e2b564777694f564a76563752576656343842483573795047727833516d2b3978665535526477672f36462b786e4f4d4573375a46784674626771514757535762304e566f4871764c4b50704f4c7870564567746765725350302b4e6b2f516664795a304e795447362b64496b414c6676555843504e3064487936704161616f6433744b5379576a4d664743414a6c774e36654c793375764259613065307678646567386676564d7239756945693051773d3d',
    '464f786155767846513450547374723275744d4c4d48384b79523077634134374b7574574a5057693935486270364142533462612f34674f3441626e4850644c6d4a4e4f2b4771535339763043316a6949686b71732b6b6e586e63595362475a592b73554e49673135455172305275696b41514a2b2f746d644839302b4a6779332f4f44523771624671564366454b597267526d695854386b4f50675a57714853344f4541776277743558335a30706e726b6d41646e5656363744736b494839574f50336454584b6c523853786545794f4b4a736c7231595838444977756a316e6751454661444477384e5944725a6d347a38524a49313874696e356732624f653248362f4c33346e47487734354c536b6a56684e32634b752f6c394c652b44484a68716f47317a4b7950357738685362585145502f5a4f6949614849616763575865325651456b324c32707a364862506d717732673d3d',
    '475264686656773254766250454b72314d4731423057626835486939437266694c677162346d50694a334357794154783975444266583130332f546a4174576b59346e533544366544326a2b434f613579685345446978317a5669717759666c7332546c5965645747446a735279575675414f45522b563363494962416e58636f736e4f624a736976346b716168304373394a3171727544326735416d354f70376e463170486b6665755436326b647875424969794844522f4e76614b61677632526951514b5a2f612b656d4e4f5546757a6f73564436576a687732324e717463756648466d2b4338652b775633746c624d3576317645582b345630397875654563565971505a2b737a3666354b4e484b5666654e5177336c6b725247724e7976476c7a336a4134576c702b496749714444627a356b306d4d7a5a7177497470446b654342594835357161396a636d664d2b506178773d3d',
    '48554a6f7037776e576d6e4b626e727a70676434636b36342f39524a7057474a4d536e686e3949685630395236476e696f6a716e2b334c61332b4c65364c50394c6f425730424b7030765949426e535263672f6461472f4550446f394f563479417436326a305a325443327376532b4934414c2b6c4d42304e7631587a535278626d454636397634344c576e51774174704e4f5a383063675245665a34507764316b7077427459685a505759725a4c30436d2b4754594631557876374239324a5861654a57576e7a6158457130516f416775454e614d373137323650393431527678446258436c4b3451627a6c77474c515a454e7648767968686f64704275732b586e70676f597346584b674875443635366543642b53646c2b64774f73694a67336d32577959387474416a7033564d35457330732b4d6c4c7a325a6d4d41413846795331316f674737635162546136614c517945413d3d',
    '49573176306877595a647a467a45727947364776457a615147792f57514173774e456b6e585542676879344e434d3754545a534f65576841333944617a704a562b586261752b61316c6f4d5342414a704767733277724d53717876507354522b556c6948764b575767434a744d7a6c3843414a34346f7863782f4572574b507851726b7078583064656971354275775a67516654597866527a3543734e61506a4177357a4b6833326463665134537a75705747724261632f376e46504b79494a357044697634416d6a6275676d6c41696a356350314735326737665548774469676e3941357334626b516b687a556a59595962713153344d5665667a696d62374d6e2b7469573041777633786b6b76747a53524e2f2f4138774d39616a69374863636b7946302b41514954715643473639624447714c684c664a7754716b586a2f37626f796f6d58642b366962656b73334e753275773d3d',
    '4a5a68322f48774a63552f424b6872776b54766c7442356e4e6f7469327254584e3268744771366674777a494b5450442b4f35303931326d3337375774484375784731657037724257684163415a42417767615148505a68476631694b51724b6f644a59366753327442637471554e764d41487a4d556b784931325670505263483949352b583651692b686674654447534738682b693259652b69336d597235644c312f446c43657256756a64525668694f6951384f49787a7476576b3357786339536363756b59324d63486b4c64723456777a6c78305953766744547a566676544c33746c3331416659362b6c464d7a4c41484951646c6175373271663249764e616b76617238752b435550755166326335417a53385645514b51464f59736831666e4571774339336a534b41643051476570784d795a473148593952305350466144337842662b30317a6a2b44326b46706f7a673d3d',
    '4b634e2b4a747636664d4b38682b7276427459635651592b556562766456352b4f6f657932427a6535757544535a69307045686264564d4d33367a536d6b38486a3250696b34374e485a306c2f78345961674870647a6d76694e37306f4f455738557771463250573641767548303169574146746750627853554b577368577942617732682b4253466536625439347a2b776d467549683053552f38444c46684b31655473323461433745516155784d74515134447a4a4b39467552514e694142584b326336544b53704e6674442f6365444234734e7262525338646943724a6279762f79746a584d38342f4868726f677778696f4166397853386e417439566d48375048304167414271494a4b6d52446156613336456d694945517a75363478435856545476453236766249795a3478472f654343414f433137706555574c706a746b464f353570644f4430783458677a424954773d3d',
    '4c653646555476726944573335627274664842533965345662554a384541676c506162346c59736546736f2b6166326c54364a42383068793335724f67433167576c706d66324c5934536f762f4b76774566314330587a3939384348474c646a514d5837524d4c33484143756c5664566741446e305a57644f6141756741667939456366634b4a6947443172314f52696d4e622b6e69686c4e385a356a7863614a74797847585a6f6b4d6758766447774b625367594a654c5876422f4d3070316d32737777624d3634794370424f6c30564250664961652f636c3069796545666d47705a4a4437434a7045754f4b5772684a763955692f565a4b69456c51786878586773726978716a36764e51357842614b6d634e305a784a307263764568734b444c3878763746375234465258374967636c6a63724b71544d4e464e7239515057574a6243506b643444544e3643507456315652413d3d',
    '4d686d4d653576636b36697a513472723867714a6c745873694a34497172484d514d592b55766c6452716a35696d4b562b76776f6354335933346a4b5a6775354a564471617a626b704c63352b6a6e48756669634b38424d5a71495a6b4932766b442f4d63694958542f567643324649714142694979553039485a644473736536364c30733854416b74545252504e534964654d7177317252307777494c776b5a307a5851476d4b504b43356371574c35766e4a3552487a44707167617375534e62344c585252716f6d376a6772517a64515a6d36595045306f4954464668694f4f3444776f2b31326a384953664756305637584e333773535673505949537451384b39616d2f636170526a6d377777367473453142373037562f7a33504e4773333964662f55474b3839516a78426a6548513642495274333337734c5970674164547a354c436763465668765768664a75475073773d3d',
	'4e6b53547066764e6e7875756f5672715a3654414e3733446f2f6d565256747a512b574545476563646f653071736547706c594f377a4d2b33336247532b6f52384564755677727761455244393865665966503168674f6131594f734347503733376d646e344533672b6f76675773377a2f2f636461573465635569586c383136372b32555564746862544c6f4173436c677376337a6547642b45667761422f374b67474b45642f447a723168386666374e4f306e4b474341316e3035317656314774475263685a694834504c61415a32776751434737725a5a33755a354352554c622f706375795474664e5566366e61565477542f5643633062485a55673445313642564170316b4e524c4c516c666c446d5574697178327342574d4f39495a677233654236466c372b382f39744a71484268765a5659773548655861613638346d6a667053746b4645765a48574631377a336f673d3d',
	'4f6d2b613046752b716f36702f79726f33543732324b576176315568344155615277544a7a645862706d5a767979783355612f316253696b333254434d636871757a3379517437384b39464e395656334365394f344562705247552b674470494c7a4e757a4f42587439377639335575392f39577952636e7959782b62735133394a316b5353706f384e31613569747a3958486f4f71613279595649636351737475343930524248434a624c2f5469734f304a6768305934505335387150744164334c68653838486c5534734261306e68686a61666d6b7a4b37433077346d733338564d7a664b3368467439554d7a67544835496d354c58346d75736f3163434e45743461767732416d75443934504e5a4d564c33576d6e37327744754478785039584b723374454d4f394b6c393937456233616e6556712b50776278785268456f4f594f64414c313351384c4d6744782b2b4e46773d3d',
	'507071682b7275767467476c5850726e55746b746559317832724375657137425369515069305161316b55713635466e2f516e623678344b33314b2b46366244686a52324c724d483731355838754e4f7365716f4f6f6f33733062512b4243556671302f2b6a393336394f7762583869482f375248586d4334387878502f6f6c426a762b6d3232793145352f4631536d5141753176567238504469714d5363717868392b4f7350694b4c513830766677306b584e705141567642673372366e53487454632f796830794e383643747463646a6a4753334b634a4c706d4b454f3035686a724f77544665736f59526c784165747267476c65736c736d2f4772454c706f6d697230556476316f4e2b79743658483471536476584b324c3863747242514e2f584a6774423931333556787a337446796b7058536b6637326b61644e5358734c53466d4b3752623649466c2f5939336c5147413d3d',
	'517357704a527567775853677573726c79484e6b476e5649396777374656686f54554e56534c4a614269506d432f5a597147504361524e77333043352f59556355537236476f6354737574683848456d576559426c4d32474969686a622b62677a6963524a3536594838687734346b56522f354c63737a4a7949543630674439494a75465342464c4d4167344d34615a646469595a3152577a2f74452f386c36476a76485a574a5162354e494351577473643337396338616742636c2b32654b797045347a395368497a453550537134713266546234736d554c73436c62367059374861375148634d694f654d717a48394771327a4550416b47442b79315a5561686b41494f557378352f704f41426d653251762b34452f6a715641594d6f3461536b633238352b3677764a505a4f2f6b45792f31454d4656395a3452654f4f3245645246457937327a4154495430465a6c704171773d3d',
	'52764377543375527a4f6563474a726b5067326175313067455766487341495055474b624269435a4e674b684c46744a5537326f35776a573379363134324e314843462b426c7366646e68723766372b41654661377844556b516e3135373074486144695650323455373078575a4d49622f334679524438643759624a4e6a415137763454785579424171474f73464e6c7469514f4a4c47684d30593361736173304d5a554f7552335450746e3248693267727265624e47695374486a4452716571663037644f4d704551706e4a73384a61594236724c5272374b4b432f714b574a4162342b6e37716d6750466235327553334d735663547a7a46727455626366766d517639786a477a305672674b5277586463386c6e6847544c5067677257754c4762304d5437432f693653305053705934734b6c434e6755615857305557667845564d34344e6c386a6454562b4a464a4a6531673d3d'    
]


# openssl rsa -in pub.pem -pubin -text -noout
e = 3  #VERY LOW!

N = '00:a4:3f:ea:ef:09:8e:e2:88:8d:4f:29:ad:c4:0c:\
    5b:44:43:e6:07:dd:5d:28:9c:3c:55:03:3e:ae:c0:\
    bc:f3:8d:57:0c:a7:eb:86:fd:85:df:ca:b8:95:11:\
    cc:86:d7:20:2a:00:4c:f7:c0:ec:83:4b:68:34:51:\
    ce:a0:73:8d:67:af:a7:74:8c:b6:f4:db:27:45:49:\
    90:ae:c2:0a:7b:5d:61:41:72:4c:48:0f:39:50:a6:\
    ee:a9:60:0c:be:fa:9f:73:14:39:a4:e5:ce:43:ea:\
    1a:c6:b3:8e:5b:90:14:42:66:cb:b5:da:db:24:fd:\
    0e:78:68:d5:df:d0:50:27:68:e1:fe:b1:b1:01:47:\
    af:ba:71:38:13:31:8d:0f:93:32:72:8b:3f:ec:f8:\
    85:77:8e:5b:8c:60:39:50:96:97:18:c3:2e:20:ad:\
    ac:30:01:2b:b3:4b:6b:2d:ce:30:99:a8:cb:16:03:\
    aa:b8:39:90:a1:3a:f4:e4:e5:6f:66:5a:68:55:f6:\
    1f:d3:59:b0:06:cb:b5:52:9c:57:44:bb:fd:45:51:\
    09:9e:10:04:36:ca:7a:f8:d1:c9:fe:99:e6:dd:04:\
    56:e9:3c:7f:c9:f9:3e:2a:81:25:be:40:3f:f8:8f:\
    31:02:51:e2:c7:53:60:a2:85:63:06:77:4d:9f:c4:\
    c9:71'

# debugging wannacry.py:
# turned out new key = previous key + 1
N = N.replace(':', '').replace(' ','')
n = int(N, 16)

offset = 1
enc_msg_1 = bytes_to_long(base64.b64decode(binascii.unhexlify(messages[0+offset])))
enc_msg_2 = bytes_to_long(base64.b64decode(binascii.unhexlify(messages[1+offset])))
enc_msg_3 = bytes_to_long(base64.b64decode(binascii.unhexlify(messages[2+offset])))
enc_msg_4 = bytes_to_long(base64.b64decode(binascii.unhexlify(messages[3+offset])))


# https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

x =  (modinv(12, n) *(enc_msg_1 + enc_msg_4 - enc_msg_2 - enc_msg_3 - 30)) % n

# print x
#print long_to_bytes(x)
# print binascii.hexlify(SHA256.new(binascii.unhexlify(messages[0+offset])).digest())
# print base64.b64encode(SHA256.new(long_to_bytes(x+offset)).digest())
# exit(0)

# ('Linux', 'debian', '3.16.0-4-586', '#1 Debian 3.16.36-1+deb8u1 (2016-09-03)', 'i686', '') 1735315642475883291798425121634177381154535250147488151897487266098115069592/
# print long_to_bytes(x)

cmd = "python wannacry.py -d {0} {1};"

#print base64.b64encode(SHA256.new(long_to_bytes(x+offset)).digest())
#print '***'

for i in range(len(messages)):
    hash = binascii.hexlify(SHA256.new(binascii.unhexlify(messages[i])).digest())
    key = base64.b64encode(SHA256.new(long_to_bytes(x + i)).digest())
    print (cmd.format(hash, key))

