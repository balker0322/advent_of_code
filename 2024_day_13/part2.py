import re

def intersection(A1, B1, C1, A2, B2, C2):

  denominator = A1 * B2 - A2 * B1
  if denominator == 0:
    return None
  
  x = (B2 * C1 - B1 * C2)
  y = (A1 * C2 - A2 * C1)
  if int(abs(x))%int(abs(denominator))!=0:
      return None
  if int(abs(y))%int(abs(denominator))!=0:
      return None

  return int(x/denominator), int(y/denominator)

def main():

    total_token = 0
    extra_num = 10000000000000

    for block in open(0).read().split('\n\n'):
        ax, ay, bx, by, px, py = [int(x) for x in re.findall(r'\d+', block)]
        px += extra_num
        py += extra_num

        ip = intersection(ax, bx, px, ay, by, py)
        
        if ip is None:
            continue
        a, b = ip
        total_token += 3*a + b

    print(total_token)


if __name__=='__main__':
    main()