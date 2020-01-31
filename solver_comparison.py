from GlobalCoordinatesToLocal import *
import datetime

BestFirstSearch_map_01 = "llllUddlluRRRRRdrUUruulldRRdldlluLuulldRurDDullDRdRRRdrUUruurrdLulDulldRddlllluurDldRRRdrUUdlllldlluRRRRRdrU"
BestFirstSearch_map_02 = "uuuRddldlllluluurDDlDRRRRdrUUruuRllldRddlllluurDldRRRdrU"
BestFirstSearch_map_03 = "lllldlluRRRRRdrUUruulldRurDlddlllllUUrrDLulDDrdLurRRRdrUUUluR"
BestFirstSearch_map_04 = "lllldlluRRRRRdrUUruulldRRdldlllluulDurrDldRRRdrUUruurrdLulDulldRddlllldlluRRRRRdrUU"
BestFirstSearch_map_05 = "lllluluurDDlDRRRRdrUUUluRRRdldldlllluurDldRRRdrU"
BestFirstSearch_map_06 = "llllUUrDuuLdldDrdLurRRRdrUUUluR"
BestFirstSearch_map_07 = "lllluulDurrDldRRRdrUUruulldRddlllldlluRRRRRdrUU"
BestFirstSearch_map_08 = "lllluurDldRRRdrUUUluRRRdldldlllldlluRRRRRdrU"
BestFirstSearch_map_09 = "lllldlUUUrrDldRRRdrUUUluR"
BestFirstSearch_map_10 = "lllluurDldRRRdrUUruulldR"
BestFirstSearch_map_11 = "lllldlluRRRRRdrUUUluRRR"
BestFirstSearch_map_12 = "lluLLdlUU"

BreadthFirstSearch_map_01 = "llllUddlluRRRRRdrUUruulldRRdldlluLuulldRurDDullDRdRRRdrUUruurrdLulDulldRddlllluurDldRRRdrUUdlllldlluRRRRRdrU"
BreadthFirstSearch_map_02 = "uuuRRdldldlllluluurDDlDRRRRdrUUruulldRddlluLulDldRRRRdrU"
BreadthFirstSearch_map_03 = "lllldlluRRRRRdrUUruulldRurDlddllllUUrDuuLdlDDrdLurRRRdrUUUluR"
BreadthFirstSearch_map_04 = "lllldlluRRRRRdrUUruulldRRdldlluLullDRurDldRRRdrUUruurrdLulDulldRddlllldlluRRRRRdrUU"
BreadthFirstSearch_map_05 = "lllluluurDDlDRRRRdrUUUluRRRdldldlluLulDldRRRRdrU"
BreadthFirstSearch_map_06 = "llllUUruLrdDllDrdLurRRRdrUUUluR"
BreadthFirstSearch_map_07 = "lluLullDRurDldRRRdrUUruulldRddlllldlluRRRRRdrUU"
BreadthFirstSearch_map_08 = "lllluurDldRRRdrUUUluRRRdldldlllldlluRRRRRdrU"
BreadthFirstSearch_map_09 = "lllldlUUUrrDldRRRdrUUUluR"
BreadthFirstSearch_map_10 = "lluLulDldRRRRdrUUruulldR"
BreadthFirstSearch_map_11 = "lllldlluRRRRRdrUUUluRRR"
BreadthFirstSearch_map_12 = "lluLLdlUU"

paths = [[BestFirstSearch_map_01,BreadthFirstSearch_map_01],
[BestFirstSearch_map_02,BreadthFirstSearch_map_02],
[BestFirstSearch_map_03,BreadthFirstSearch_map_03],
[BestFirstSearch_map_04,BreadthFirstSearch_map_04],
[BestFirstSearch_map_05,BreadthFirstSearch_map_05],
[BestFirstSearch_map_06,BreadthFirstSearch_map_06],
[BestFirstSearch_map_07,BreadthFirstSearch_map_07],
[BestFirstSearch_map_08,BreadthFirstSearch_map_08],
[BestFirstSearch_map_09,BreadthFirstSearch_map_09],
[BestFirstSearch_map_10,BreadthFirstSearch_map_10],
[BestFirstSearch_map_11,BreadthFirstSearch_map_11],
[BestFirstSearch_map_12,BreadthFirstSearch_map_12]]

move_time ={'p': 2.5883273945914373,
            'r': 2.340702384710312,
            'b': 4.057445287704468,
            'l': 2.8050299286842346,
            'f': 1.4083196699619294}

for path in paths:
    timeDiff =(datetime.timedelta(seconds=sum([move_time[a] for a in globalToLocal(path[1])]))-datetime.timedelta(seconds=sum([move_time[a] for a in globalToLocal(path[0])]))).total_seconds()
    print("(BestFS,BreadthFS) Equal: "+str(path[0]==path[1])+"\t Length: "+str((len(path[0]),len(path[0])))+"\tTime difference(Beadth-Best): "+str(timeDiff))

for path in paths:
    print(datetime.timedelta(seconds=sum([move_time[a] for a in globalToLocal(path[1])])).total_seconds(),datetime.timedelta(seconds=sum([move_time[a] for a in globalToLocal(path[0])])).total_seconds())


print(globalToLocal(BreadthFirstSearch_map_07))
print(globalToLocal(BreadthFirstSearch_map_07))
