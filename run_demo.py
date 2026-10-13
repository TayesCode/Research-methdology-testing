from benchmark import run_benchmark

results = run_benchmark()

print("ASR:", results["asr"])
print("Calls:", results["calls"])
print("Cost:", results["cost"])
print("Store Size:", results["size"])
print("Poisons:", results["poisons"])