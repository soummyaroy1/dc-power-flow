# Info

This is a simple DC power-flow calculator for a N-bus/N-branch system. DC power-flow studies are an alternative to more precise but intensive methods like Newton-Raphson or Gauss-Seidal. This makes them perfect for lightweight realtime calculations, in which you are only concerned about detecting thermal violations. This script is based on the methodology found in the following paper, orginally authored by Iowa State University's Jim McCalley:

http://home.engineering.iastate.edu/~jdm/ee553/DCPowerFlowEquations.pdf

# Usage

The script takes as an input two flat files: bus.txt and branch.txt. (Examples of which can be found in the repository above.) The first line of each files contains headers describing the formatting of the input data. 

**bus.txt** should be formatted as such:

```
Bus Number, Per Unit Gen, Per Unit Load
1,2,0
2,2,1
3,0,4
4,1,0
```

**branch.txt** should be formatted as such:

```
From Bus, To Bus, Branch Suceptance
1,2,-10
1,3,-10
1,4,-10
2,3,-10
3,4,-10
```

**Note: Files must be in the same directory as the script.**

Thanks!
