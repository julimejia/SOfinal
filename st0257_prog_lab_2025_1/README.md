Para correr mi proyecto solo es necesario lo siguiente 

Unicamente para windows 

$env:PYTHONPATH = ";C:\Users\david\OneDrive\Escritorio\SeptimoSemestre\OS\FinalSo\st0257_prog_lab_2025_1"
$env:RENDEZVOUSMODULE = "pysync.RendezvousDEchange"
$env:PRODCONSMODULE = "pysync.gen_prod_cons"
cd C:\Users\david\OneDrive\Escritorio\SeptimoSemestre\OS\FinalSo\st0257_prog_lab_2025_1

python -m unittest test.prod_cons_test_sync    
python -m unittest test.prod_cons_test_basic
python -m unittest test.rendezvous_test_basic   
python -m unittest test.rendezvous_test_sync


Busque sus variantes para linux 
