import os

def sellAction(sellOpt, resultList, singleDate):
	curResult = resultList[-1]
	if curResult[4] == 10:
		print("Error: No Hold Stock")
		return None

	partXCode = sellOpt[-1]
	partXPrice = sellOpt[3]
	partXShare = sellOpt[2]
	partXDate = singleDate

	part = [partXCode, partXPrice, partXShare, partXDate]

	sellResult = sell(curResult, part, singleDate)
	if sellResult:
		update(sellResult)

	return sellResult

def sell(curResult, part, singleDate):
	partCodeIndex = (6, 10, 14, 18, 22, 26, 30, 34, 38, 42)
	sellResult =[]
	for n in curResult:
		sellResult.append(n)
	#sellResult = curResult
	
	for num in partCodeIndex:
		if curResult[num] == part[0]:
			#print(sellResult)
			#print(part)

			sellResult[0] = singleDate
			sellResult[1] = curResult[1] + 1
			sellResult[2] = curResult[2] - curResult[num + 1] * curResult[num + 2] + part[1] * curResult[num + 2]
			sellResult[3] = curResult[3] + part[1] * curResult[num + 2]
			sellResult[4] = curResult[4] + 1
			sellResult[5] = sellResult[3] / sellResult[4]
			sellResult[46] = "sell"
			sellResult[47] = part[0]
			sellResult[48] = part[1]
			sellResult[49] = sellResult[num + 2]
			sellResult[50] = sellResult[num + 3]
			sellResult[num] = 0
			sellResult[num + 1] = 0
			sellResult[num + 2] = 0
			sellResult[num + 3] = 0
			#print(sellResult)
			return sellResult
	return None

def update(sellResult):
	partCodeIndex = (6, 10, 14, 18, 22, 26, 30, 34, 38, 42)
	#print(sellResult)
	holdNum = 10 - sellResult[4]
	if holdNum == 0:
		return sellResult

	for num in xrange(0,holdNum):
		indexNum = partCodeIndex[num]
		if sellResult[indexNum] == 0:
			del sellResult[indexNum: indexNum + 4]
			#print("del")

			sellResult.insert(42, 0)
			sellResult.insert(43, 0)
			sellResult.insert(44, 0)
			sellResult.insert(45, 0)

def buyAction(buyOptList, resultList, singleDate):
	qOptList = []
	qOptList = chooseBuyOpt(buyOptList)
	if qOptList:
		#curResult = []
		curResult = resultList[-1]
		leftPart = curResult[4]
		sortBuyOpt(qOptList, leftPart)
		buyResultList =[]

		for buyOpt in qOptList:
			buyResult = buy(curResult, buyOpt, singleDate)
			resultList.append(buyResult)
			curResult = resultList[-1]
			
def chooseBuyOpt(buyOptList):
	qOptList = []
	for buyOpt in buyOptList:
		# decide what to choosepy
		if buyOpt[6] > 0 and buyOpt[7] > 0.00:
		# just decide from last op rate
		# if buyOpt[5] > 1:
			qOptList.append(buyOpt)

	return qOptList

#need to complete this function
def sortBuyOpt(qOptList, leftPart):
	lenNum = len(qOptList)
	if lenNum > leftPart:
		del qOptList[leftPart: lenNum]

def buy(curResult, buyOpt, singleDate):
	partCodeIndex = (6, 10, 14, 18, 22, 26, 30, 34, 38, 42)
	buyResult = []
	for n in curResult:
		buyResult.append(n)

	partXCode = buyOpt[-1]
	partXPrice = buyOpt[3]
	partXShare = curResult[5] / buyOpt[3]
	partXDate = singleDate

	part = [partXCode, partXPrice, partXShare, partXDate]

	holdNum = 10 - curResult[4]
	indexNum = partCodeIndex[holdNum]

	buyResult[0] = singleDate
	buyResult[1] = curResult[1] + 1
	buyResult[3] = curResult[3] - part[1] * part[2]
	buyResult[4] = curResult[4] - 1
	if buyResult[4]:
		buyResult[5] = buyResult[3] / buyResult[4]
	else :
		buyResult[5] = 0
	for n in xrange(0,4):
		buyResult[indexNum + n] = part[n]
	buyResult[46] = "buy"
	buyResult[47] = part[0]
	buyResult[48] = part[1]
	buyResult[49] = part[2]
	buyResult[50] = part[3]

	return buyResult

def test(testList):
	del testList[3: 5]


# test ===================
if __name__=='__main__':

	testList = range(1, 10)

	print(testList)
	test(testList)
	print(testList)

	#print(fileDict)
	#for filePath, tbl in fileDict.items():
	#	print(filePath)
	#	print(tbl)
	