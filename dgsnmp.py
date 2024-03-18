"""
Implementing scalar MIB objects
+++++++++++++++++++++++++++++++

Listen and respond to SNMP GET/SET/GETNEXT/GETBULK queries with
the following options:

* SNMPv2c
* with SNMP community "public"
* serving custom Managed Object Instance defined within this script
* allow read access only to the subtree where the custom MIB object resides
* over IPv4/UDP, listening at 127.0.0.1:161

The following Net-SNMP commands will walk this Agent:

| $ snmpwalk -v2c -c public 127.0.0.1 .1.3.6

"""#
import configparser
import json
#import sys
from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.proto.api import v2c

# Create SNMP engine
snmpEngine = engine.SnmpEngine()

# Transport setup

# UDP over IPv4
config.addTransport(
    snmpEngine,
    udp.domainName,
    udp.UdpTransport().openServerMode(('0.0.0.0', 161))
)

# SNMPv2c setup

# SecurityName <-> CommunityName mapping.
config.addV1System(snmpEngine, 'my-area', 'public')

# Allow read MIB access for this user / securityModels at VACM
#config.addVacmUser(snmpEngine, 2, 'my-area', 'noAuthNoPriv', (1, 3, 6, 5))
config.addVacmUser(snmpEngine, 2, 'my-area', 'authNoPriv', (1, 3, 6, 1, 4, 1, 99999))

# Create an SNMP context
snmpContext = context.SnmpContext(snmpEngine)

# --- create custom Managed Object Instance ---

mibBuilder = snmpContext.getMibInstrum().getMibBuilder()

MibScalar, MibScalarInstance = mibBuilder.importSymbols(
    'SNMPv2-SMI', 'MibScalar', 'MibScalarInstance'
)


class MyStaticMibScalarInstance(MibScalarInstance):

    config = configparser.RawConfigParser()
    config.optionxform = str
    config.read('SNMPParam.conf')
    details_dict = dict(config.items('SNMPPARAMS'))
    
    ##noinspection PyUnusedLocal,PyUnusedLocal
    def getValue(self, name, idx, **context):
        # Opening JSON file
        f = open('data.json')
        
        # returns JSON object as 
        # a dictionary
        data = json.load(f)
        y=''
        for x in self.details_dict:
            value=self.details_dict[str(x)]
            try:
                if str(self.name) == value:
                    y=data[x]
                    print(y)
            except Exception as e:
                           print("Exception Occured")
                           print("Error is",e)

        return self.getSyntax().clone(
            y
        )



    # def getValue(self, name, idx, **context):
    #     if self.syntax is not None:
    #         return self.getSyntax().clone(y)
    # def setValue(self, value, name, idx):
    #     y=value
    #     print(y)

mibBuilder.exportSymbols(
    'demo', 
    MibScalar((1,3,6,1,4,1,99999), v2c.OctetString()),
    #MibScalar((1, 3, 6, 5, 1), v2c.OctetString()).setMaxAccess('readwrite'),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,1,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,2,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,3,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,4,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,5,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,6,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,7,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,8,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,9,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,10,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,11,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,12,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,13,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,14,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,15,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,16,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,17,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,18,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,19,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,20,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,21,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,22,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,23,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,24,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,25,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,26,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,27,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,28,0), v2c.TimeTicks()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,29,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,30,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,31,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,32,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,33,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,35,0), v2c.TimeTicks()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,36,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,37,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,38,0), v2c.Integer32()),
    MyStaticMibScalarInstance((1,3,6,1,4,1,99999), (1,39,0), v2c.Integer32())

)

# --- end of Managed Object Instance initialization ----

# Register SNMP Applications at the SNMP engine for particular SNMP context
cmdrsp.GetCommandResponder(snmpEngine, snmpContext)
#cmdrsp.SetCommandResponder(snmpEngine, snmpContext)
cmdrsp.NextCommandResponder(snmpEngine, snmpContext)
cmdrsp.BulkCommandResponder(snmpEngine, snmpContext)

# Register an imaginary never-ending job to keep I/O dispatcher running forever
snmpEngine.transportDispatcher.jobStarted(1)

# Run I/O dispatcher which would receive queries and send responses
try:
    snmpEngine.transportDispatcher.runDispatcher()

finally:
    snmpEngine.transportDispatcher.closeDispatcher()
