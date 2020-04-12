from mrjob.job import MRJob
from mrjob.step import MRStep


class checkForGreen(MRJob):
	#l = dict()

	def steps(self):
		return [MRStep(mapper=self.mapper_check_green,reducer=self.reducer_get_green)]

	def mapper_check_green(self, _, line):
		(pincode, percentage) = line.split(',')
		percentage = float(percentage)
		if(percentage > 60):
			p = round(percentage, 1)
			yield pincode, percentage

	def reducer_get_green(self, key, values):
		yield key, sum(values)

if __name__ == '__main__':
	checkForGreen.run()
