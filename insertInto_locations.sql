INSERT INTO 'locations' ('icao_code','iata_code','location_name','city','country','local_timezone_utc')
VALUES
    -- United Kingdom & Ireland
    ('EGLL','LHR','London Heathrow','London','United Kingdom','+00:00'),
    ('EGKK','LGW','London Gatwick','London','United Kingdom','+00:00'),
    ('EGSS','STN','London Stansted','London','United Kingdom','+00:00'),
    ('EGGW','LCY','London City','London','United Kingdom','+00:00'),
    ('EGCC','MAN','Manchester Airport','Manchester','United Kingdom','+00:00'),
    ('EGPH','EDI','Edinburgh Airport','Edinburgh','United Kingdom','+00:00'),
    ('EGAA','BFS','Belfast International','Belfast','United Kingdom','+00:00'),
    ('EGAC','BHD','George Best Belfast City','Belfast','United Kingdom','+00:00'),
    ('EGGP','LPL','Liverpool John Lennon','Liverpool','United Kingdom','+00:00'),
    ('EGNX','EMA','East Midlands Airport','Nottingham','United Kingdom','+00:00'),
    ('EGNM','LBA','Leeds Bradford Airport','Leeds','United Kingdom','+00:00'),
    ('EGPE','INV','Inverness Airport','Inverness','United Kingdom','+00:00'),
    ('EGHI','SOU','Southampton Airport','Southampton','United Kingdom','+00:00'),
    ('EGPD','ABZ','Aberdeen Airport','Aberdeen','United Kingdom','+00:00'),
    ('EGNT','NCL','Newcastle Airport','Newcastle','United Kingdom','+00:00'),
    ('EGNS','IOM','Isle of Man Airport','Douglas','United Kingdom','+00:00'),
    ('EGJJ','JER','Jersey Airport','Jersey','United Kingdom','+00:00'),
    ('EGJB','GCI','Guernsey Airport','Guernsey','United Kingdom','+00:00'),
    ('EGTE','EXT','Exeter Airport','Exeter','United Kingdom','+00:00'),
    ('EIDW','DUB','Dublin','Dublin','Ireland','+00:00'),

    -- France
    ('LFPG','CDG','Charles de Gaulle','Paris','France','+01:00'),
    ('LFPO','ORY','Orly','Paris','France','+01:00'),
    ('LFBP','BVA','Paris Beauvais-Tillé','Beauvais','France','+01:00'),
    ('LFBO','TLS','Toulouse Blagnac','Toulouse','France','+01:00'),
    ('LFMN','NCE','Nice Côte d''Azur','Nice','France','+01:00'),

    -- Germany
    ('EDDF','FRA','Frankfurt Airport','Frankfurt','Germany','+01:00'),
    ('EDDM','MUC','Munich Airport','Munich','Germany','+01:00'),
    ('EDDH','HAM','Hamburg Airport','Hamburg','Germany','+01:00'),
    ('EDDL','DUS','Düsseldorf Airport','Düsseldorf','Germany','+01:00'),
    ('EDDK','CGN','Cologne Bonn Airport','Cologne','Germany','+01:00'),

    -- Spain & Portugal
    ('LEMD','MAD','Adolfo Suárez Madrid-Barajas','Madrid','Spain','+01:00'),
    ('LEBL','BCN','Barcelona-El Prat','Barcelona','Spain','+01:00'),
    ('LEPA','PMI','Palma de Mallorca','Palma','Spain','+01:00'),
    ('LEMG','AGP','Málaga-Costa del Sol','Málaga','Spain','+01:00'),
    ('GCTS','TFS','Tenerife South','Tenerife','Spain','+00:00'),
    ('LPPT','LIS','Lisbon Portela','Lisbon','Portugal','+00:00'),
    ('LPPR','OPO','Porto Airport','Porto','Portugal','+00:00'),

    -- Italy
    ('LIRF','FCO','Leonardo da Vinci-Fiumicino','Rome','Italy','+01:00'),
    ('LIMC','MXP','Milan Malpensa','Milan','Italy','+01:00'),
    ('LIRA','CIA','Rome Ciampino','Rome','Italy','+01:00'),
    ('LIPE','BLQ','Bologna Guglielmo Marconi','Bologna','Italy','+01:00'),
    ('LIRN','NAP','Naples International','Naples','Italy','+01:00'),

    -- Northern Europe / Scandinavia
    ('EKCH','CPH','Copenhagen Airport','Copenhagen','Denmark','+01:00'),
    ('ESSA','ARN','Stockholm Arlanda','Stockholm','Sweden','+01:00'),
    ('EFHK','HEL','Helsinki Airport','Helsinki','Finland','+02:00'),
    ('ENGM','OSL','Oslo Gardermoen','Oslo','Norway','+01:00'),
    ('ENBR','BGO','Bergen Airport','Bergen','Norway','+01:00'),

    -- Central & Eastern Europe
    ('LKPR','PRG','Václav Havel Airport Prague','Prague','Czech Republic','+01:00'),
    ('EPWA','WAW','Warsaw Chopin Airport','Warsaw','Poland','+01:00'),
    ('LHBP','BUD','Budapest Ferenc Liszt','Budapest','Hungary','+01:00'),
    ('LJLJ','LJU','Ljubljana Jože Pučnik','Ljubljana','Slovenia','+01:00'),
    ('LYBE','BEG','Belgrade Nikola Tesla','Belgrade','Serbia','+01:00'),

    -- Southeastern Europe & Balkans
    ('LGAV','ATH','Elefthérios Venizélos','Athens','Greece','+02:00'),
    ('LYPG','TGD','Podgorica Airport','Podgorica','Montenegro','+01:00'),
    ('LWSK','SKP','Skopje International','Skopje','North Macedonia','+01:00'),
    ('TIV','TIV','Tivat Airport','Tivat','Montenegro','+01:00'),
    ('LBSF','SOF','Sofia Airport','Sofia','Bulgaria','+02:00'),

    -- Benelux, Switzerland & Austria
    ('EHAM','AMS','Amsterdam Schiphol','Amsterdam','Netherlands','+01:00'),
    ('EBBR','BRU','Brussels Airport','Brussels','Belgium','+01:00'),
    ('LSZH','ZRH','Zurich Airport','Zürich','Switzerland','+01:00'),
    ('LOWW','VIE','Vienna International','Vienna','Austria','+01:00'),
    ('LOWS','SZG','Salzburg Airport','Salzburg','Austria','+01:00'),

    -- Iceland
    ('BIKF','KEF','Keflavík International','Reykjavík','Iceland','+00:00'),

    -- Azores (Portugal)
    ('LPPD','PDL','João Paulo II Airport','Ponta Delgada','Portugal (Azores)','-01:00'),

    -- Greenland (Kingdom of Denmark)
    ('BGSF','SFJ','Kangerlussuaq Airport','Kangerlussuaq','Greenland','-03:00'),
    ('BGGH','GOH','Nuuk Airport','Nuuk','Greenland','-02:00'),

    -- Turkey
    ('LTFM','IST','Istanbul Airport','Istanbul','Turkey','+03:00'),
    ('LTFJ','SAW','Sabiha Gökçen','Istanbul','Turkey','+03:00'),

    -- Cyprus
    ('LCLK','LCA','Larnaca International','Larnaca','Cyprus','+02:00'),
    ('LCPH','PFO','Paphos International','Paphos','Cyprus','+02:00'),

    -- North Africa
    ('DAAG','ALG','Houari Boumediene','Algiers','Algeria','+01:00'),
    ('DTTA','TUN','Tunis-Carthage Airport','Tunis','Tunisia','+01:00'),
    ('HECA','CAI','Cairo International','Cairo','Egypt','+02:00'),
    ('GMMN','CMN','Mohammed V International','Casablanca','Morocco','+01:00'),
    ('GMFF','FEZ','Fès-Saïs Airport','Fès','Morocco','+01:00');


/* 
    This was generated using ChatGPT as per exceptions in the worksheet
    After giving it an example for London Heathrow
    I then asked for a selection of airports from across Europe and North Africa
    plus some airports in the Azures and greenland to have some timezones ofset negativly
    from UTC Corrections were then made for escaping ' and 
*/