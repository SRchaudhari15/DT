import json, unittest, datetime

with open("./data-1.json", "r") as f:
  jsonData1 = json.load(f)
with open("./data-2.json", "r") as f:
  jsonData2 = json.load(f)
with open("./data-result.json", "r") as f:
  jsonExpectedResult = json.load(f)


def convertFromFormat1(jsonObject):
  # create a nested dictionary

  # IMPLEMENT: Conversion From Type 1
  result = {
    "deviceID": jsonObject["deviceID"],
    "deviceType": jsonObject["deviceType"],
    "timestamp": jsonObject["timestamp"],
    "location": {
      "country": jsonObject["location"][0:5],
      "city": jsonObject["location"][6:11],
      "area": jsonObject["location"][12:33],
      "factory": jsonObject["location"][34:55],
      "section": jsonObject["location"][56:65]
    },
    "data": {
      "status": jsonObject["operationStatus"],
      "temperature": jsonObject["temp"]
    }
  }

  return result


def convertFromFormat2(jsonObject):

  # IMPLEMENT: Conversion From Type 1
  convert_date = datetime.datetime.strptime(jsonObject['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')
  new_timestamp = round((convert_date - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)
  
  result = {
    "deviceID": jsonObject["device"]["id"],
    "deviceType": jsonObject["device"]["type"],
    "timestamp": new_timestamp,
    "location": {
      "country": jsonObject["country"],
      "city": jsonObject["city"],
      "area": jsonObject["area"],
      "factory": jsonObject["factory"],
      "section": jsonObject["section"]
    },
    "data": {
      "status": jsonObject["data"]["status"],
      "temperature": jsonObject["data"]["temperature"]
    }
  }

  return result


def main(jsonObject):

  result = {}

  if (jsonObject.get('device') == None):
    result = convertFromFormat1(jsonObject)
  else:
    result = convertFromFormat2(jsonObject)

  return result


class TestSolution(unittest.TestCase):

  def test_sanity(self):

    result = json.loads(json.dumps(jsonExpectedResult))
    self.assertEqual(result, jsonExpectedResult)

  def test_dataType1(self):

    result = main(jsonData1)
    self.assertEqual(result, jsonExpectedResult,
                     'Converting from Type 1 failed')

  def test_dataType2(self):

    result = main(jsonData2)
    self.assertEqual(result, jsonExpectedResult,
                     'Converting from Type 2 failed')


if __name__ == '__main__':
  unittest.main()
