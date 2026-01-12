def computegrade(score):
    if score >= 0.9:
        return '5,0'
    elif score >= 0.8:
        return '4,5'
    elif score >= 0.7:
        return '4,0'
    elif score >= 0.6:
        return '3,5'
    elif score >= 0.5:
        return '3,0'
    else:
        return '2,0'

if __name__ == "__main__":
    print(computegrade(0.95))
    print(computegrade(0.5))
    print(computegrade(0.2))