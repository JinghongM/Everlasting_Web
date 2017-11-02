import re

class calculator():
    _heightMap = {'\"' : 'inches', 'inches' : 'inches', '\'': 'inches', 'cm' : 'cm', 'CM' : 'cm' }
    _weightMap = {'kg' : 'kg', 'KG' : 'kg', 'lbs' : 'lbs', 'LBS' : 'lbs'}
    _unitSet = {'h': _heightMap, 'w': _weightMap}

    _heightRules = {'cm': 1, 'inches': 2.54}
    _weightRules = {'kg': 1, 'lbs': 0.453592}
    _ruleSet = {'h': _heightRules, 'w': _weightRules}

    def __init__(self, unitSet = None, ruleSet = None):
        if unitSet is not None:
            self._unitSet = unitSet
        if ruleSet is not None:
            self._ruleSet = ruleSet

    def checkUnit(self, data, u):
        unitMap = self._unitSet.get(u)
        for key in unitMap:
          	if key in data:
                return unitMap.get(key)
        return None

    def calValue(self, data, u):
        unit = self.checkUnit(data, u)
        rule = self._ruleSet.get(u)
        num = getNum(data)[0]
        return rule.get(unit) * num

    def getNum(self, data):
        return float(re.findall(r'\d+\.?\d+'))