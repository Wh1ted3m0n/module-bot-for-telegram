
class Cache:
   
    def record_habr(self,habr):
        self.idhabr= habr
        with open('core/cache/habr_cache.txt',"a+") as file:
            
            if file.read().strip() == self.idhabr:
                print("Nothing news habr")
                return False
            print("there are news habr")
            file.seek(0)
            file.write(self.idhabr)
            file.truncate()
            return True
    def record_opennet(self,opennet):
        self.idopennet - opennet
        with open('core/cache/openet_cache.txt',"a+") as file:
            
            if file.read().strip() == self.idopennet:
                print("Nothing news opennet")
                return False
            print("there are news openet")
            file.seek(0)
            file.write(self.idopennet)
            file.truncate()
            return True




                
            file.seek(0)
            
