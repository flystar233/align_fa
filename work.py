import click
import matplotlib.pyplot as plt
import numpy as np

@click.command("main", help="Make the alignment diagram of two fasta sequences")
@click.option(
    "-a", "--fasta", type=click.Path(exists=True), help="the alignment fasta"
    )
@click.option(
    "-s", "--score", default="Default12",type=click.Choice(['Default12','blast']),help="Scoring Matrix"
    )
def main(fasta,score):
	try:
		with open(fasta) as IN:
			Dict = {}
			for line in IN:
				if line[0] == '>':
					key = line[1:-1]
					Dict[key] = []
				else:
					Dict[key].append(line.strip("\n"))
			for key, value in Dict.items():
				Dict[key] = ''.join(value)

			key1,key2 = Dict.keys()
			fasta1 = Dict[key1].upper()
			fasta2 = Dict[key2].upper()
			result=[]
			if score == 'Default12':
				for x,y in zip(fasta1,fasta2):
					if x == y:
						if x=='-' or y=='-':
							result.append(2)
						else:
							result.append(-1)
					elif x != y:
						if x=='-' or y=='-':
							result.append(2)
						else:
							result.append(1)
					else:
						pass
			else:
				for x,y in zip(fasta1,fasta2):
					if x == y:
						if x=='-' or y=='-':
							result.append(5)
						else:
							result.append(-5)
					elif x != y:
						if x=='-' or y=='-':
							result.append(5)
						else:
							result.append(4)
					else:
						pass

			for num,i in enumerate(result):
				if num == 0:
					pass
				else:
					result[num]=result[num-1]+result[num]

			x = range(len(result))
			f1 = np.polyfit(x, result, 1)
			p1 = np.poly1d(f1)
			yvals1 = p1(x)

			f3 = np.polyfit(x, result, 3)
			p3 = np.poly1d(f3)
			yvals3 = p3(x)
			plt.figure(figsize=(10,7.2))
			plt.style.use('ggplot')
			plt.xlabel("base site")
			if 200 < len(result) < 1000:
				plt.scatter(x,result,s=0.5)
				plt.plot(x,result,lw=1)
			elif 0 < len(result) < 200:
				plt.scatter(x,result,s=5)
				plt.plot(x,result)
			else:
				plt.scatter(x,result,s=0.1)
				plt.plot(x,result,lw=1)
			plt.plot(x, yvals1,label=p1)
			plt.plot(x, yvals3)
			plt.legend()
			if score == 'Default12':
				plt.savefig("result_Default12.pdf")
			else:
				plt.savefig("result_blast.pdf")

	except TypeError:
			print("File not found,please input existing file or use option --help")
	except FileNotFoundError :
			print("File not found,please input existing file or use option --help")
		
if __name__ == "__main__":
        main()

