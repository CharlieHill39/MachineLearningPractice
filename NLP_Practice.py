'''
中文分词-逆向最大匹配法
'''
class RMM:
	'''
	作用：加载词典文件到内存，并且记录词典中最长词的长度
	参数：
		dict_path：词典路径
	'''
	def __init__(self,dict_path):
		#存储字典到内存，并去重
		self.dict = set()
		#词典中最长词条的长度
		self.max_len = 0

		with open(dict_path,"r",encoding="utf8") as f:
			for word in f:
				word = word.strip()
				if not word:
					continue
				self.dict.add(word)
				word_num = len(word)
				if self.max_len < word_num:
					self.max_len = word_num

	def cut(self,text):
		result = []
		index = len(text)
		while index > 0:
			word = None
			for size in range(self.max_len,0,-1):
				if index-size < 0:
					continue

				pice = text[(index-size):index]
				if pice in self.dict:
					word = pice
					result.append(word)
					index -= size
					break
			if word is None:
				index -= 1
				result.append(text[index:index+1])
		return result[::-1]

def main():
	text = "南京市长江大桥"
	rmm = RMM("./data/cut_dict.utf8")
	rs = rmm.cut(text)
	print(rs)

main()




