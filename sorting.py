'''
The complexity of sorting algorithm for this case is O(n^2).
This is beacuse there are two main loops in the sorting algorithm that run n times (where n is the length of linked list)
since each loop runs n times. As the loops are nested, the complexity becomes n*n or n^2.
All the other statements are executed in constant time and therefore can be ignored.

Hence the complexity of sorting algorithm for this case is O(n^2).
'''

class LinkedList:
    def __init__(self, data):
        self.label = data[0][0]
        self.value = data[0][1]
        self.tail = None if (len(data) == 1) else LinkedList(data[1:])
    

    def printList(self):
        t = self
        while (t is not None): #will run n times where n is the length of linked list
            print(t.label,"--",t.value)
            t = t.tail
        
    def sortList(self):
        curr = self      #constant time
        next = curr.tail #constant time

        while (curr is not None): #loop will run n times
            next = curr.tail
            while (next is not None): # loop will run n times
                if (curr.value < next.value):

                    tempLabel = curr.label # each statement will be 
                    tempValue = curr.value # executed n * n times
                                           # beacuse two loops are being run nested
                    curr.label = next.label
                    curr.value = next.value


                    next.label = tempLabel
                    next.value = tempValue

                next = next.tail
            curr = curr.tail


countries = LinkedList([("Ukraine",41879904),("Brunei",442400),("Christmas Island (Australia)",1928),("Mauritius",1265985),("Lesotho",2007201),("Guatemala",16604026),("British Virgin Islands (UK)",30030),("Malta",493559),("Greenland (Denmark)",56081),("Guernsey (UK)",62792),("Ethiopia",98665000),("Suriname",581372),("Turkmenistan",6031187),("American Samoa (US)",56700),("French Polynesia (France)",275918),("Equatorial Guinea",1358276),("Solomon Islands",680806),("Burundi",10953317),("Abkhazia",244832),("Rwanda",12374397),("Iceland",364260),("Monaco",38300),("Namibia",2458936),("United States",329532925),("Brazil",211402908),("Finland",5527573),("Armenia",2957500),("Wallis and Futuna (France)",11700),("Cuba",11209628),("Guyana",782766),("Oman",4664790),("Aruba (Netherlands)",112309),("Nauru",11000),("Sri Lanka",21803000),("Myanmar",54339766),("United Arab Emirates",9890400),("Hungary",9772756),("Norfolk Island (Australia)",1756),("Cambodia",15288489),("Fiji",884887),("Benin",11733059),("Egypt",100264508),("Northern Cyprus",351965),("Angola",31127674),("Barbados",287025),("Trinidad and Tobago",1363985),("Colombia",49395678),("Turks and Caicos Islands (UK)",41369),("Norway",5367580),("Kiribati",120100),("Kosovo",1795666),("Azerbaijan",10067108),("Romania",19405156),("Kyrgyzstan",6533500),("Peru",32131400),("Australia",25680766),("Faroe Islands (Denmark)",52124),("Turkey",83154997),("Georgia",3723464),("Singapore",5703600),("Eswatini",1093238),("Saint Vincent and the Grenadines",110608),("East Timor",1387149),("Tuvalu",10200),("Pakistan",219313520),("Bahrain",1543300),("Paraguay",7152703),("Jersey (UK)",106800),("Slovakia",5456362),("Mongolia",3313049),("Argentina",44938712),("Jordan",10660256),("Saint Barthélemy (France)",9793),("Andorra",77543),("Bangladesh",168456310),("Saint Martin (France)",35746),("FS Micronesia",104468),("South Sudan",12778250),("Artsakh",148000),("Slovenia",2094060),("Senegal",16209125),("Ivory Coast",25823071),("Syria",17500657),("Montserrat (UK)",4989),("Philippines",108505959),("Laos",7123205),("Gibraltar (UK)",33701),("Iran",83371987),("Bahamas",385340),("Mauritania",4077347),("Portugal",10276617),("Madagascar",26251309),("Malawi",19129952),("Central African Republic",5496011),("Saint Kitts and Nevis",52823),("Ghana",30280811),("Honduras",9158345),("Belarus",9408400),("India",1361140893),("Estonia",1328360),("Nicaragua",6460411),("Mali",20250833),("Zambia",17885422),("S\u00e3o Tom\u00e9 and Pr\u00edncipe",201784),("Cura\u00e7ao (Netherlands)",158665),("Jamaica",2726667),("Northern Mariana Islands (US)",56200),("Vanuatu",304500),("Kuwait",4420110),("Cameroon",26545864),("Netherlands",17456281),("Saudi Arabia",34218169),("Dominican Republic",10358320),("Japan",125950000),("Djibouti",1078373),("Antigua and Barbuda",96453),("Morocco",35871167),("Nigeria",206139587),("Iraq",39127900),("South Korea",51780579),("Pitcairn Islands (UK)",50),("US Virgin Islands (US)",104578),("Ireland",4921500),("Sierra Leone",7901454),("Cyprus",875900),("Palestine",4976684),("Luxembourg",626108),("Falkland Islands (UK)",3198),("France",67076000),("Bolivia",11469896),("Panama",4218808),("Seychelles",97625),("Guinea-Bissau",1604528),("Puerto Rico (US)",3193694),("Anguilla (UK)",14869),("Macau (China)",679600),("North Macedonia",2077132),("Saint Helena, Ascension",5633),("Sweden",10338368),("Kazakhstan",18683712),("China",1402247960),("Italy",60238522),("Israel",9186750),("Uzbekistan",34131625),("Guam (US)",172400),("Dominica",71808),("Malaysia",32752760),("New Zealand",4978784),("Cape Verde",550483),("Uruguay",3518552),("Belgium",11524454),("Kenya",47564296),("Saint Pierre and Miquelon (France)",6008),("Uganda",40299300),("Yemen",29825968),("Nepal",29996478),("Switzerland",8603899),("Sint Maarten (Netherlands)",40614),("Tonga",100651),("Algeria",43000000),("Haiti",11577779),("Zimbabwe",15159624),("North Korea",25450000),("Congo",5518092),("Belize",408487),("Czech Republic",10693939),("Poland",38379000),("San Marino",33574),("Tanzania",55890747),("Tokelau (NZ)",1400),("Saint Lucia",178696),("Cook Islands (NZ)",15200),("Mozambique",30066648),("Indonesia",266911900),("Grenada",112003),("Burkina Faso",20870060),("Western Sahara",582463),("New Caledonia (France)",282200),("Albania",2845955),("Greece",10724599),("Bosnia and Herzegovina",3301000),("Montenegro",622359),("Russia",146745098),("Samoa",200874),("Comoros",873724),("United Kingdom",66435550),("Taiwan",23604265),("Vatican City",799),("Austria",8902600),("Lebanon",6825442),("Latvia",1906800),("Mexico",126577691),("Venezuela",32219521),("Papua New Guinea",8935000),("Chad",16244513),("Canada",37996639),("Maldives",374775),("Denmark",5822763),("Tajikistan",9127000),("Isle of Man (UK)",83314),("Afghanistan",32225560),("Germany",83149300),("Vietnam",96208984),("Eritrea",3497117),("Spain",47100396),("Costa Rica",5058007),("Cayman Islands (UK)",65813),("Niger",22314743),("Liechtenstein",38749),("Gambia",2347706),("Hong Kong (China)",7500700),("Sudan",42432665),("Tunisia",11722038),("\u00c5land Islands (Finland)",29885),("DR Congo",89561404),("Bulgaria",6951482),("Liberia",4475353),("Botswana",2338851),("Palau",17900),("Niue (NZ)",1520),("Thailand",66494417),("South Africa",58775022),("Lithuania",2793471),("Gabon",2172579),("Libya",6871287),("Transnistria",469000),("Moldova",2681735),("South Ossetia",53532),("Guinea",12218357),("El Salvador",6486201),("Croatia",4076246),("Qatar",2747282),("Serbia",6963764),("Togo",7538000),("Ecuador",17466864),("Cocos (Keeling) Islands (Australia)",538),("Chile",19107216),("Bermuda (UK)",64027),("Somalia",15893219),("Bhutan",741672),("Marshall Islands",55500)])


def main():
    print ("Before Sorting\n")
    print ("--------\n")
    countries.printList()
    countries.sortList()
    print ("--------\n")
    print ("After Sorting\n")
    print ("--------\n")
    countries.printList()
if __name__ == "__main__":
    main()