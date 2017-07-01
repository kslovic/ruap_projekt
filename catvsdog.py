import sys
sys.path.insert(0,'D:\\\home\\Python27\\Lib\\site-packages')
print(sys.path)
import cv2                 # working with, mainly resizing, images
import os                  # dealing with directories
import sys
import numpy
import urllib2
import json 
from skimage import feature
TEST_DIR = 'uploads'
IMG_SIZE = 200

def process_pic():
    try:
        data = sys.argv[1]
    except:
        print "ERROR"
        sys.exit(1)
    path = os.path.join(TEST_DIR,data)
    img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
    (H, hogImage)  = feature.hog(img, orientations=8, pixels_per_cell=(16, 16),cells_per_block=(1, 1), visualise=True, feature_vector=True) 
    numpy.set_printoptions(threshold=numpy.nan)
    x = numpy.array(H)
    y=numpy.array(map(str, x))
    y=y.tolist()
    y.insert( 0, '')
    # If you are using Python 3+, import urllib instead of urllib2

    data =  {

            "Inputs": {

                    "input1":
                        {
                                "ColumnNames": ["Col1", "Col2", "Col3", "Col4", "Col5", "Col6", "Col7", "Col8", "Col9", "Col10", "Col11", "Col12", "Col13", "Col14", "Col15", "Col16", "Col17", "Col18", "Col19", "Col20", "Col21", "Col22", "Col23", "Col24", "Col25", "Col26", "Col27", "Col28", "Col29", "Col30", "Col31", "Col32", "Col33", "Col34", "Col35", "Col36", "Col37", "Col38", "Col39", "Col40", "Col41", "Col42", "Col43", "Col44", "Col45", "Col46", "Col47", "Col48", "Col49", "Col50", "Col51", "Col52", "Col53", "Col54", "Col55", "Col56", "Col57", "Col58", "Col59", "Col60", "Col61", "Col62", "Col63", "Col64", "Col65", "Col66", "Col67", "Col68", "Col69", "Col70", "Col71", "Col72", "Col73", "Col74", "Col75", "Col76", "Col77", "Col78", "Col79", "Col80", "Col81", "Col82", "Col83", "Col84", "Col85", "Col86", "Col87", "Col88", "Col89", "Col90", "Col91", "Col92", "Col93", "Col94", "Col95", "Col96", "Col97", "Col98", "Col99", "Col100", "Col101", "Col102", "Col103", "Col104", "Col105", "Col106", "Col107", "Col108", "Col109", "Col110", "Col111", "Col112", "Col113", "Col114", "Col115", "Col116", "Col117", "Col118", "Col119", "Col120", "Col121", "Col122", "Col123", "Col124", "Col125", "Col126", "Col127", "Col128", "Col129", "Col130", "Col131", "Col132", "Col133", "Col134", "Col135", "Col136", "Col137", "Col138", "Col139", "Col140", "Col141", "Col142", "Col143", "Col144", "Col145", "Col146", "Col147", "Col148", "Col149", "Col150", "Col151", "Col152", "Col153", "Col154", "Col155", "Col156", "Col157", "Col158", "Col159", "Col160", "Col161", "Col162", "Col163", "Col164", "Col165", "Col166", "Col167", "Col168", "Col169", "Col170", "Col171", "Col172", "Col173", "Col174", "Col175", "Col176", "Col177", "Col178", "Col179", "Col180", "Col181", "Col182", "Col183", "Col184", "Col185", "Col186", "Col187", "Col188", "Col189", "Col190", "Col191", "Col192", "Col193", "Col194", "Col195", "Col196", "Col197", "Col198", "Col199", "Col200", "Col201", "Col202", "Col203", "Col204", "Col205", "Col206", "Col207", "Col208", "Col209", "Col210", "Col211", "Col212", "Col213", "Col214", "Col215", "Col216", "Col217", "Col218", "Col219", "Col220", "Col221", "Col222", "Col223", "Col224", "Col225", "Col226", "Col227", "Col228", "Col229", "Col230", "Col231", "Col232", "Col233", "Col234", "Col235", "Col236", "Col237", "Col238", "Col239", "Col240", "Col241", "Col242", "Col243", "Col244", "Col245", "Col246", "Col247", "Col248", "Col249", "Col250", "Col251", "Col252", "Col253", "Col254", "Col255", "Col256", "Col257", "Col258", "Col259", "Col260", "Col261", "Col262", "Col263", "Col264", "Col265", "Col266", "Col267", "Col268", "Col269", "Col270", "Col271", "Col272", "Col273", "Col274", "Col275", "Col276", "Col277", "Col278", "Col279", "Col280", "Col281", "Col282", "Col283", "Col284", "Col285", "Col286", "Col287", "Col288", "Col289", "Col290", "Col291", "Col292", "Col293", "Col294", "Col295", "Col296", "Col297", "Col298", "Col299", "Col300", "Col301", "Col302", "Col303", "Col304", "Col305", "Col306", "Col307", "Col308", "Col309", "Col310", "Col311", "Col312", "Col313", "Col314", "Col315", "Col316", "Col317", "Col318", "Col319", "Col320", "Col321", "Col322", "Col323", "Col324", "Col325", "Col326", "Col327", "Col328", "Col329", "Col330", "Col331", "Col332", "Col333", "Col334", "Col335", "Col336", "Col337", "Col338", "Col339", "Col340", "Col341", "Col342", "Col343", "Col344", "Col345", "Col346", "Col347", "Col348", "Col349", "Col350", "Col351", "Col352", "Col353", "Col354", "Col355", "Col356", "Col357", "Col358", "Col359", "Col360", "Col361", "Col362", "Col363", "Col364", "Col365", "Col366", "Col367", "Col368", "Col369", "Col370", "Col371", "Col372", "Col373", "Col374", "Col375", "Col376", "Col377", "Col378", "Col379", "Col380", "Col381", "Col382", "Col383", "Col384", "Col385", "Col386", "Col387", "Col388", "Col389", "Col390", "Col391", "Col392", "Col393", "Col394", "Col395", "Col396", "Col397", "Col398", "Col399", "Col400", "Col401", "Col402", "Col403", "Col404", "Col405", "Col406", "Col407", "Col408", "Col409", "Col410", "Col411", "Col412", "Col413", "Col414", "Col415", "Col416", "Col417", "Col418", "Col419", "Col420", "Col421", "Col422", "Col423", "Col424", "Col425", "Col426", "Col427", "Col428", "Col429", "Col430", "Col431", "Col432", "Col433", "Col434", "Col435", "Col436", "Col437", "Col438", "Col439", "Col440", "Col441", "Col442", "Col443", "Col444", "Col445", "Col446", "Col447", "Col448", "Col449", "Col450", "Col451", "Col452", "Col453", "Col454", "Col455", "Col456", "Col457", "Col458", "Col459", "Col460", "Col461", "Col462", "Col463", "Col464", "Col465", "Col466", "Col467", "Col468", "Col469", "Col470", "Col471", "Col472", "Col473", "Col474", "Col475", "Col476", "Col477", "Col478", "Col479", "Col480", "Col481", "Col482", "Col483", "Col484", "Col485", "Col486", "Col487", "Col488", "Col489", "Col490", "Col491", "Col492", "Col493", "Col494", "Col495", "Col496", "Col497", "Col498", "Col499", "Col500", "Col501", "Col502", "Col503", "Col504", "Col505", "Col506", "Col507", "Col508", "Col509", "Col510", "Col511", "Col512", "Col513", "Col514", "Col515", "Col516", "Col517", "Col518", "Col519", "Col520", "Col521", "Col522", "Col523", "Col524", "Col525", "Col526", "Col527", "Col528", "Col529", "Col530", "Col531", "Col532", "Col533", "Col534", "Col535", "Col536", "Col537", "Col538", "Col539", "Col540", "Col541", "Col542", "Col543", "Col544", "Col545", "Col546", "Col547", "Col548", "Col549", "Col550", "Col551", "Col552", "Col553", "Col554", "Col555", "Col556", "Col557", "Col558", "Col559", "Col560", "Col561", "Col562", "Col563", "Col564", "Col565", "Col566", "Col567", "Col568", "Col569", "Col570", "Col571", "Col572", "Col573", "Col574", "Col575", "Col576", "Col577", "Col578", "Col579", "Col580", "Col581", "Col582", "Col583", "Col584", "Col585", "Col586", "Col587", "Col588", "Col589", "Col590", "Col591", "Col592", "Col593", "Col594", "Col595", "Col596", "Col597", "Col598", "Col599", "Col600", "Col601", "Col602", "Col603", "Col604", "Col605", "Col606", "Col607", "Col608", "Col609", "Col610", "Col611", "Col612", "Col613", "Col614", "Col615", "Col616", "Col617", "Col618", "Col619", "Col620", "Col621", "Col622", "Col623", "Col624", "Col625", "Col626", "Col627", "Col628", "Col629", "Col630", "Col631", "Col632", "Col633", "Col634", "Col635", "Col636", "Col637", "Col638", "Col639", "Col640", "Col641", "Col642", "Col643", "Col644", "Col645", "Col646", "Col647", "Col648", "Col649", "Col650", "Col651", "Col652", "Col653", "Col654", "Col655", "Col656", "Col657", "Col658", "Col659", "Col660", "Col661", "Col662", "Col663", "Col664", "Col665", "Col666", "Col667", "Col668", "Col669", "Col670", "Col671", "Col672", "Col673", "Col674", "Col675", "Col676", "Col677", "Col678", "Col679", "Col680", "Col681", "Col682", "Col683", "Col684", "Col685", "Col686", "Col687", "Col688", "Col689", "Col690", "Col691", "Col692", "Col693", "Col694", "Col695", "Col696", "Col697", "Col698", "Col699", "Col700", "Col701", "Col702", "Col703", "Col704", "Col705", "Col706", "Col707", "Col708", "Col709", "Col710", "Col711", "Col712", "Col713", "Col714", "Col715", "Col716", "Col717", "Col718", "Col719", "Col720", "Col721", "Col722", "Col723", "Col724", "Col725", "Col726", "Col727", "Col728", "Col729", "Col730", "Col731", "Col732", "Col733", "Col734", "Col735", "Col736", "Col737", "Col738", "Col739", "Col740", "Col741", "Col742", "Col743", "Col744", "Col745", "Col746", "Col747", "Col748", "Col749", "Col750", "Col751", "Col752", "Col753", "Col754", "Col755", "Col756", "Col757", "Col758", "Col759", "Col760", "Col761", "Col762", "Col763", "Col764", "Col765", "Col766", "Col767", "Col768", "Col769", "Col770", "Col771", "Col772", "Col773", "Col774", "Col775", "Col776", "Col777", "Col778", "Col779", "Col780", "Col781", "Col782", "Col783", "Col784", "Col785", "Col786", "Col787", "Col788", "Col789", "Col790", "Col791", "Col792", "Col793", "Col794", "Col795", "Col796", "Col797", "Col798", "Col799", "Col800", "Col801", "Col802", "Col803", "Col804", "Col805", "Col806", "Col807", "Col808", "Col809", "Col810", "Col811", "Col812", "Col813", "Col814", "Col815", "Col816", "Col817", "Col818", "Col819", "Col820", "Col821", "Col822", "Col823", "Col824", "Col825", "Col826", "Col827", "Col828", "Col829", "Col830", "Col831", "Col832", "Col833", "Col834", "Col835", "Col836", "Col837", "Col838", "Col839", "Col840", "Col841", "Col842", "Col843", "Col844", "Col845", "Col846", "Col847", "Col848", "Col849", "Col850", "Col851", "Col852", "Col853", "Col854", "Col855", "Col856", "Col857", "Col858", "Col859", "Col860", "Col861", "Col862", "Col863", "Col864", "Col865", "Col866", "Col867", "Col868", "Col869", "Col870", "Col871", "Col872", "Col873", "Col874", "Col875", "Col876", "Col877", "Col878", "Col879", "Col880", "Col881", "Col882", "Col883", "Col884", "Col885", "Col886", "Col887", "Col888", "Col889", "Col890", "Col891", "Col892", "Col893", "Col894", "Col895", "Col896", "Col897", "Col898", "Col899", "Col900", "Col901", "Col902", "Col903", "Col904", "Col905", "Col906", "Col907", "Col908", "Col909", "Col910", "Col911", "Col912", "Col913", "Col914", "Col915", "Col916", "Col917", "Col918", "Col919", "Col920", "Col921", "Col922", "Col923", "Col924", "Col925", "Col926", "Col927", "Col928", "Col929", "Col930", "Col931", "Col932", "Col933", "Col934", "Col935", "Col936", "Col937", "Col938", "Col939", "Col940", "Col941", "Col942", "Col943", "Col944", "Col945", "Col946", "Col947", "Col948", "Col949", "Col950", "Col951", "Col952", "Col953", "Col954", "Col955", "Col956", "Col957", "Col958", "Col959", "Col960", "Col961", "Col962", "Col963", "Col964", "Col965", "Col966", "Col967", "Col968", "Col969", "Col970", "Col971", "Col972", "Col973", "Col974", "Col975", "Col976", "Col977", "Col978", "Col979", "Col980", "Col981", "Col982", "Col983", "Col984", "Col985", "Col986", "Col987", "Col988", "Col989", "Col990", "Col991", "Col992", "Col993", "Col994", "Col995", "Col996", "Col997", "Col998", "Col999", "Col1000", "Col1001", "Col1002", "Col1003", "Col1004", "Col1005", "Col1006", "Col1007", "Col1008", "Col1009", "Col1010", "Col1011", "Col1012", "Col1013", "Col1014", "Col1015", "Col1016", "Col1017", "Col1018", "Col1019", "Col1020", "Col1021", "Col1022", "Col1023", "Col1024", "Col1025", "Col1026", "Col1027", "Col1028", "Col1029", "Col1030", "Col1031", "Col1032", "Col1033", "Col1034", "Col1035", "Col1036", "Col1037", "Col1038", "Col1039", "Col1040", "Col1041", "Col1042", "Col1043", "Col1044", "Col1045", "Col1046", "Col1047", "Col1048", "Col1049", "Col1050", "Col1051", "Col1052", "Col1053", "Col1054", "Col1055", "Col1056", "Col1057", "Col1058", "Col1059", "Col1060", "Col1061", "Col1062", "Col1063", "Col1064", "Col1065", "Col1066", "Col1067", "Col1068", "Col1069", "Col1070", "Col1071", "Col1072", "Col1073", "Col1074", "Col1075", "Col1076", "Col1077", "Col1078", "Col1079", "Col1080", "Col1081", "Col1082", "Col1083", "Col1084", "Col1085", "Col1086", "Col1087", "Col1088", "Col1089", "Col1090", "Col1091", "Col1092", "Col1093", "Col1094", "Col1095", "Col1096", "Col1097", "Col1098", "Col1099", "Col1100", "Col1101", "Col1102", "Col1103", "Col1104", "Col1105", "Col1106", "Col1107", "Col1108", "Col1109", "Col1110", "Col1111", "Col1112", "Col1113", "Col1114", "Col1115", "Col1116", "Col1117", "Col1118", "Col1119", "Col1120", "Col1121", "Col1122", "Col1123", "Col1124", "Col1125", "Col1126", "Col1127", "Col1128", "Col1129", "Col1130", "Col1131", "Col1132", "Col1133", "Col1134", "Col1135", "Col1136", "Col1137", "Col1138", "Col1139", "Col1140", "Col1141", "Col1142", "Col1143", "Col1144", "Col1145", "Col1146", "Col1147", "Col1148", "Col1149", "Col1150", "Col1151", "Col1152", "Col1153"],
                                "Values": [y, ]
                                },        },
                "GlobalParameters": {
                        "Shuffle examples": "",
                        }
                }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/108212f5c19146b09aee41da39445841/services/a6c63b3894204568b53ca0cfde8d2a59/execute?api-version=2.0&details=true'
    api_key = 'YXED68rPxREXtPWtduXPFXIYPV4wTyAYcnnVCXkrRQt/tVWDBNbfwhZ5ucqJkrVkPvXTryupLEJPJ540/lWLlw==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib2.Request(url, body, headers) 

    try:
        response = urllib2.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
            # req = urllib.request.Request(url, body, headers) 
            # response = urllib.request.urlopen(req)

        result = response.read()
        result = result.split(',')
        result=result[-2]
        print(result) 
    except urllib2.HTTPError, error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read()))                 
process_pic()
