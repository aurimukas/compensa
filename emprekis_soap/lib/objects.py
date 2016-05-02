from django.conf import settings

from .cypher import CompensaEncryption
from suds.client import Client


# -*- coding: utf-8 -*-
CarDataSource = ['None', 'MotorBiuro', 'SERegitra', 'Other']
CarUsageCategory = ['Private', 'Taxi', 'Special', 'HazardousCargo', 'Other']
UsageRegion = ['Lithuania', 'BalticStates', 'EuropeWithoutGBAndIE', 'EuropeWithGBAndIE']
AdditionalDiscountType = ['None', 'OC', 'AC', 'OP', 'NW', 'AS', 'WD', 'GR', 'OCAC', 'OCACOP', 'ALL']
ModInsuranceSumType = ['Undefined', 'Renewal', 'Accounting', 'Actual']
ModPackageType = ['Undefined', 'OnlyTheft', 'TheftAndDamage', 'TheftAndDamageWithCarReplacement', 'OnlyTotalDestruction']
OwnPartsAC = ['None', 'OwnPart300', 'OwnPart500', 'OwnPart1000', 'OwnPart3000', 'OwnPart5000', 'OwnPart300LTL']
OwnPartsTheftAC = ['None', 'OwnPart5', 'OwnPart10', 'OwnPart15']
TerritorialSalesTaxAC = ['None', 'EuNorwaySwitzerland', 'GeographicalEurope']
TariffOPvariants = ['Agreement', 'Driver']

cypher = CompensaEncryption(init_cipher=True)


class Region:
    internalId = 0
    name = ''
    versisId = 0
    zoneAC = 0
    zoneOC = 0

    def __init__(self, internalId=0, name='', versisId=0, zoneAC=0, zoneOC=0):
        self.internalId = internalId
        self.name = name
        self.versisId = versisId
        self.zoneAC = zoneAC
        self.zoneOC = zoneOC

    def __unicode__(self):
        return "%s(%s): versisId->%s, zone AC-OC: %s-%s" % (self.internalId, self.name,
            self.versisId, self.zoneAC, self.zoneOC
        )



class MotorInsurance(object):
    cypher = None
    service_user = ''
    service_pass = ''
    crypted_user = None
    crypted_pass = None
    service_address = ''
    client = None

    def __init__(self, user=None, pwd=None, service=None):
        self.init_cypher()
        if not user:
            self.service_user = settings.EMPREKIS_SOAP_USER if hasattr(settings, 'EMPREKIS_SOAP_USER') else ''
        else:
            self.service_user = user

        if not pwd:
            self.service_pass = settings.EMPREKIS_SOAP_PASS if hasattr(settings, 'EMPREKIS_SOAP_PASS') else ''
        else:
            self.service_pass = pwd

        if not service:
            self.service_address = settings.EMPREKIS_SOAP_URL if hasattr(settings, 'EMPREKIS_SOAP_URL') else ''
        else:
            self.service_address = service


    def init_cypher(self):
        if not self.cypher:
            self.cypher = CompensaEncryption(init_cipher=True)

    def create_client(self):
        return Client(self.service_address, location=self.service_address)

    def get_crypted_username(self):
        if not self.crypted_user:
            self.crypted_user = self.cypher.encrypt(self.service_user)
        return self.crypted_user

    def get_crypted_pass(self):
        if not self.crypted_pass:
            self.crypted_pass = self.cypher.encrypt(self.service_pass)
        return self.crypted_pass

    def decrypt(self, str):
        return self.cypher.decrypt(str)

    def GetCarOwnerData(self, NumberType=None, PersonalCode='', VehicleNumber="",
                        PersonType=0, IsSearch=False):
        print("vehicle nr {0}".format(VehicleNumber), "type: {0}".format(type(VehicleNumber)))
        client = self.create_client()
        print("Client:", client)
        vehicleNumberType = client.factory.create('VehicleNumberType')

        request = client.factory.create('RequestOfGetCarAndOwnerDataArgs')
        request.Login = self.get_crypted_username()
        request.Password = self.get_crypted_pass()

        request_args = client.factory.create('GetCarAndOwnerDataArgs')
        request_args.NumberType = vehicleNumberType.RegistrationVehicleNumberType if not NumberType else NumberType
        #request_args.PersonalCode = str(PersonalCode)
        request_args.PersonalCode = "{0}".format(PersonalCode)
        #request_args.VehicleNumber = str(VehicleNumber)
        request_args.VehicleNumber = "{0}".format(VehicleNumber)
        request_args.PersonType = int(PersonType)
        request_args.IsSearch = bool(IsSearch)

        request.Data = request_args

        return client.service.GetCarWidthAveragePriceAndOwnerData(request)
        #return self.client.service.GetCarWidthAveragePriceAndOwnerData(request)
        #return self.client.service.GetCarAndOwnerData(request)


class GetYearsArgs:

    def __init__(self, vehicleGroup=0):
        self.VehicleGroup = int(vehicleGroup)

    def __unicode__(self):
        return {
            'VehicleGroup': self.VehicleGroup
        }


class GetYearsRequest:
    def __init__(self, getYearsArgs=None):
        super(GetYearsRequest, self).__init__()
        if getYearsArgs:
            self.Data = getYearsArgs
        else:
            self.Data = GetYearsArgs