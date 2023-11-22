section .text
global _start
_start:
  mov cl, 68

  mov rax, 1
  mov rdi, 1
  mov rsi, bt
  mov rdx, 1
  syscall

  mov rax, 60
  xor rdi, rdi
  syscall

section .data
bt: BYTE [cx]

