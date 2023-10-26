#!/bin/sh

(
cat <<'EOF'
int main()
{
    printf("flag4{'a_piece_of_cake'}\n");
    return 0;
}
EOF
) > runme.c

gcc -o runme runme.c
rm runme.c
chmod 400 runme
