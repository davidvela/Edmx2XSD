

# Functions
def getXMLElements(path): 
    with open(path, 'r') as file:
        fileXMXr = file.read().replace('\n', '')

    # split on    from: '<value', 1 ) to '</value>', 1 )  
    start = '<value'
    end   = '</value>'

    # elements = split at '</'  => I don't get the type   
    elements = fileXMXr.split(start, 1)[1]
    elements = elements.split(end,1)[0]
    elements = elements.split("<")
    tmp = []
    for e in elements: 
        if e[0] != '/' : #&& e[0] <> '' : 
                eName = e.split('>',1)
                name = eName[0]
                name.replace("/", "")                tmp.append(name)
                
    print(len(tmp))
    return tmp

def getXSDElements(path): 

    with open(path, 'r') as file:
        fileXSD = file.read().replace('\n', '')
    elements = fileXSD.split("<xsd:element")
    tmp = []
    for e in elements: 
        if e[0:5] == ' name': 
                eName = e.split('name="')
                eName = eName[1].split('"', 1)
                tmp.append(eName[0])
                #print(eName[0])
    print(len(tmp))
    return tmp

path = '../DYNAMICS_ODataV4_edmx.xml'
with open(path, 'r') as file:
    fileEdmx = file.read().replace('\n', '')
    
    
def getEntity(entityName): 
    entityData = fileEdmx.split('<EntityType Name='+ entityName)
    entityData = entityData[1].split("</EntityType>", 1)

    print(len(entityData))
    entityData  = entityData[0] 
    return entityData

def getAttribute(attr, entityData ): 
    attributeData = entityData.split(attr)
    tmp = []
    for at in attributeData: 
    #     print(prop[0:5])
        if at[0:5] == ' Name': 
            #print(prop)
            atName = at.split(' Name="')
            atName = atName[1].split('"', 1)
            name = atName[0]
            if name[0] == '_': 
                name = name[1:]
            tmp.append(name)
            #print(NProp[0])
    print(len(tmp))
    return tmp

def printBasic4XSD(propertyNames, 
                   keys=[], 
                   snms = '"http://namespace.com/project1"',
                   sd1  = '"DT_Name "',  
                   sd2  = 'DT Project'): 
    print(len(propertyNames))
    print('<?xml version="1.0" encoding="UTF-8"?><xsd:schema targetNamespace='+ snms )
    print('xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns='+snms+'>'  )
    print('<xsd:complexType name='+sd1+'>'   )
    print('<xsd:annotation><xsd:documentation xml:lang="EN">'+sd2+'</xsd:documentation></xsd:annotation>' )
    print('<xsd:sequence>' )
    print('<xsd:element name="value">' )
    print('<xsd:complexType><xsd:sequence>' )
    for p in propertyNames:
        if p in keys: minOccur = "1"
        else :  minOccur = "0"
        print('<xsd:element name="{}" type="xsd:string" minOccurs="{}"/>'.format(p,minOccur))

    print( '</xsd:sequence></xsd:complexType>')    
    print('</xsd:element>' )
    print('</xsd:sequence>' )
    print('</xsd:complexType>') 


if __name__ == "__main__":
    #executions
    pathXML = '../MSDynamicsPortfolioResp.xml'
    xml = getXMLElements(pathXML)

    pathXSD = '../DYN_DT_PortfolioResponse.xsd'
    elements = getXSDElements(pathXSD)

    Property = []
    PropertyRef = []
    NavigationProperty = []
    PropertyOO = []

    alt_portfolio = getEntity('"alt_portfolio"')
    Property = getAttribute("Property" , alt_portfolio)
    PropertyRef = getAttribute("PropertyRef" , alt_portfolio)
    NavigationProperty = getAttribute("NavigationProperty" , alt_portfolio)
    PropertyOO = getAttribute("<Property" , alt_portfolio)

    alt_turnover = getEntity('"alt_turnover"')
    Property = getAttribute("Property" , alt_turnover)
    PropertyRef = getAttribute("PropertyRef" , alt_turnover)
    NavigationProperty = getAttribute("NavigationProperty" , alt_turnover)
    PropertyOO = getAttribute("<Property" , alt_turnover)


    sNamespace = '"http://namespace.com/1233"' 
    sd1  = '"DT_XSD_Name"'
    sd2 = 'DT Project'
    # printBasic4XSD(PropertyOO, PropertyRef , sNamespace , sd1, sd2 )
    # minOccurs="1" ==> keys
    # printBasic4XSD(xml, [] , sNamespace , sd1, sd2 )
