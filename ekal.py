class Bunga(object):
   def __init__(self, m, p, k):
      self.bungaMerah = m
      self.bungaPutih = p
      self.bungaKuning = k

   def cetakData(self):
      print("Bunga Merah\t: ", self.bungaMerah)
      print("Bunga Putih\t: ", self.bungaPutih)
      print("Bunga Kuning\t: ", self.bungaKuning)

# mendefinisikan kelas turunan (subclass)
class jenisBunga(Bunga):
   def __init__(self, m, p, k, u):
      self.bungaMerah = m
      self.bungaPutih = p
      self.bungaKuning = k
      self.bungaUngu = u
      
   def cetakData(self):
        print("Bunga Merah\t: ", self.bungaMerah)
        print("Bunga Putih\t: ", self.bungaPutih)
        print("Bunga Kuning\t: ", self.bungaKuning)
        print("Bunga Ungu\t: ", self.bungaUngu)

def main():
   # membuat objek ruangan
   jenisbunga1 = jenisBunga("Mawar", "Melati", "Matahari", "Anggrek")

   # menggunakan objek
   jenisbunga1.cetakData()

if __name__ == "__main__":
   main()
