
    def mpg_by_make(self):
        makeCounts=dict()
        mpgSum= defaultdict(int)
        mpgByMake= defaultdict(int)
        f = attrgetter('make', 'model', 'year', 'mpg')
        Makes=[]
        for car in self.data:
            make=f(car)[0]
            Makes+=[make]

            mpg=f(car)[-1]
            mpgSum[make] += mpg


        makeCounts = {make:Makes.count(make) for make in Makes}



        for make1, count in makeCounts.items():
            for make2, MPGsum in mpgSum.items():
                if year1==year2:
                    mpgByMake[make1] = (MPGsum/count)

        return mpgByMake

    def mpg_by_make(self):
        f = attrgetter('make', 'model', 'year', 'mpg')
        for car in self.data:
            make=f(car)[0]
            mpg=f(car)[-1]


            mpgSum[make] += mpg
            print("mpg sum" , mpgSum)
        makeCount=Counter(make)
        print("make count" , makeCount)
        for make1, count in yearCount.items():
            for make2, MPGsum in mpgSum.items():
                if make1==make2:
                    mpgByMake[make1] += (MPGsum/count)
        return mpgByMake
