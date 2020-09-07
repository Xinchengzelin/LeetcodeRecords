// 方法1
public int climbStairs(int n)
{
    if (n == 1)
    {
        return 1;
    }
    int[][] dp = new int[n + 1][4]; // 1. 升维: 上一步走的步数， prev
    dp[1][1] = 1;
    dp[1][2] = 0;
    dp[1][3] = 0;
    dp[2][1] = 0;
    dp[2][2] = 1;
    dp[2][3] = 0;
    dp[3][1] = 1;
    dp[3][2] = 1;
    dp[3][3] = 1;

    for (int i = 4; i <= n; ++i)
    {
        for (int j = 1; j <= 3; ++j)
        {
            for (int k = 1; k <= 3; ++k)
            {
                if (j != k)
                {
                    dp[i][j] += dp[i - j][k];
                }
            }
        }
    }
    return dp[n][1] + dp[n][2] + dp[n][3];
}
// 走法2
public int climbStairs2(int n, int[] steps)
{
    int[][] sum = new int[n + 1][steps.length + 1];
    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j < steps.length; ++j)
        {
            int last = steps[j];
            if (last > i)
            {
                // 当前step步长已经跨出去了
                continue;
            }
            if (last == i)
            {
                // 当前step步长正好等于当前台阶级数，走法+1
                sum[i][j] += 1;
                continue;
            }
            for (int k = 0; k < steps.length; ++k)
            {
                int prev = steps[k];
                if (last == prev)
                    continue;
                sum[i][j] += sum[i - last][k]; // last != prev
            }
        }
    }
    int result = 0;
    for (int j = 0; j < steps.length; ++j)
    {
        result += sum[n][j];
    }
    return result;
}
