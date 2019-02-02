#!/usr/bin/env bash

CODE=A_S_D_F_G_H_J_K_L_Q_W_E_R_T_Z_U_I_O_P

echo "character 16 is:"
echo $CODE | cut -d'_' -f 5

echo "character 17 is:"
echo $CODE | cut -d'_' -f 18
