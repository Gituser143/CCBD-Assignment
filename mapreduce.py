from mrjob.job import MRJob
from mrjob.step import MRStep


class checkForGreen(MRJob):
	#l = dict()

	def steps(self):
		return [MRStep(mapper=self.mapper_get_green,reducer=self.reducer_check_green)]

	def mapper_get_green(self, _, line):
		(pincode, percentage) = line.split(',')
		p = round(float(percentage), 1)
		yield pincode + ' : ' + str(p), float(percentage)

	def reducer_check_green(self, key, values):
		if(sum(values) > 30) :
			yield key, sum(values)

if __name__ == '__main__':
	checkForGreen.run()
