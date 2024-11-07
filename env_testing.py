import benchmark
import autonomous_optimizer

def main():
    quadratic_dataset = [benchmark.convex_quadratic() for _ in range(90)]

    env = autonomous_optimizer.Environment(quadratic_dataset, 40, 20)
    env.reset(seed=42)

if __name__ == "__main__":
    main()