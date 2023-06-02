from ortools.sat.python import cp_model

#---------------------------------------------------
# data
#---------------------------------------------------

data = {'bin':{'h':60,'w':40},
        'cat1':{'w': 7,'h':12,'items':10},
        'cat2':{'w': 9,'h': 3,'items':10},
        'cat3':{'w': 5,'h':14,'items':10},
        'cat4':{'w':13,'h': 9,'items':10},
        'cat5':{'w': 6,'h': 8,'items': 5},
        'cat6':{'w':20,'h': 5,'items': 5}}

#
# extract data for easier access
#

# bin width and height
H = data['bin']['h']
W = data['bin']['w']

# h,w,cat for each item
h = [data[cat]['h'] for cat in data if cat!='bin' for i in range(data[cat]['items'])]
w = [data[cat]['w'] for cat in data if cat!='bin' for i in range(data[cat]['items'])]
cat = [cat for cat in data if cat!='bin' for i in range(data[cat]['items'])]
n = len(h)  # number of items
m = 10      # number of bins

#---------------------------------------------------
# or-tools model
#---------------------------------------------------


model = cp_model.CpModel()

"""
As do the current version this Algorthm is not available for the users.
"""

# x1,x2 and y1,y2 are start and end
x1 = [model.NewIntVar(0,W-w[i],f'x1.{i}') for i in range(n)]
x2 = [model.NewIntVar(w[i],W,f'x2.{i}') for i in range(n)]

y1 = [model.NewIntVar(0,H-h[i],f'y1.{i}') for i in range(n)]
y2 = [model.NewIntVar(h[i],H,f'y2.{i}') for i in range(n)]

# interval variables
xival = [model.NewIntervalVar(x1[i],w[i],x2[i],f'xival{i}') for i in range(n)]
yival = [model.NewIntervalVar(y1[i],h[i],y2[i],f'yival{i}') for i in range(n)]

# bin numbers
b = [model.NewIntVar(0,m,f'b{i}') for i in range(n)]

# b2[(i,j)] = true if b[i]=b[j] for i<j
b2 = {(i,j):model.NewBoolVar(f'b2.{i}.{j}') for j in range(n) for i in range(j)}

# used bins
u = [model.NewBoolVar(f'u{k}') for k in range(m)]


#
# constraints
#

# no overlap for items in same bin
for j in range(n):
  for i in range(j):
    model.Add(b[i] != b[j]).OnlyEnforceIf(b2[(i,j)].Not())
    model.AddNoOverlap2D([xival[i],xival[j]],[yival[i],yival[j]]).OnlyEnforceIf(b2[(i,j)])

# used bin
for i in range(n):
  for k in range(m):
    model.Add(b[i]<k).OnlyEnforceIf(u[k].Not())

# objective
model.Minimize(sum([u[k] for k in range(m)]))


#
# solve model
#
solver = cp_model.CpSolver()
rc = solver.Solve(model)
print(rc)
print(solver.StatusName())