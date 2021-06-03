from string import Template
import string
import os
import json
from pathlib import Path


BASEDIR = os.path.dirname(__file__)
COIN_SCRIPT_DIR= os.path.join(BASEDIR, '../coinScript')
CONFIG_JSON = os.path.join(BASEDIR, '../config/config.json')	


def render(src, dest, **kw):
	t = Template(open(src, 'r').read())
	with open(dest, 'w') as f:
		f.write(t.substitute(**kw))

def getTemplate(templateName):
	configTemplate = os.path.join(BASEDIR, "../template/" + templateName)
	return configTemplate

def createCoinScript():
	coinTemplate=getTemplate("templateCoin.sol")

	with open(CONFIG_JSON) as json_file:
		data= json.load(json_file)
	filename=data['name'] + "-coinScript.sol"
	render(coinTemplate, COIN_SCRIPT_DIR + "/" + filename,
	name = data['name'],
	symbol = data['symbol'],
	totalSupply = data['totalSupply'],
	decimals= data['decimals']
	)

	print(filename+" :token script is created successfully in directory ./coinScript")

if __name__ == "__main__" :
	createCoinScript()
