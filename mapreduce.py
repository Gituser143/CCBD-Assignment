from mrjob.job import MRJob
from mrjob.step import MRStep

class checkForGreen(MRJob):

	def steps(self):
		return [MRStep(mapper = self.mapper_get_green, reducer = self.reducer_check_green)]

	def mapper_get_green(self, _, line):
		(pincode, percentage) = line.split(',')
		percentage = float(percentage)
		if(percentage > 30) :
			yield pincode, float(percentage)

	def reducer_check_green(self, key, values):

			yield key, sum(values)

if __name__ == '__main__':
	checkForGreen.run()
