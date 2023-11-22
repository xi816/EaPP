section .text
puti:
  mov r9, -3689348814741910323
  sub rsp, 40
  mov BYTE [rsp+31], 0
  lea rcx, [rsp+30]
.L2:
  mov rax, rdi
  lea r8, [rsp+32]
  mul r9
  mov rax, rdi
  sub r8, rcx
  shr rdx, 3
  lea rsi, [rdx+rdx*4]
  add rsi, rsi
  sub rax, rsi
  add eax, 48
  mov BYTE [rcx], al
  mov rax, rdi
  mov rdi, rdx
  mov rdx, rcx
  sub rcx, 1
  cmp rax, 9
  ja .L2
  lea rax, [rsp+32]
  mov edi, 1
  sub rdx, rax
  xor eax, eax
  lea rsi, [rsp+32+rdx]
  mov rdx, r8
  mov rax, 1
  syscall
  add rsp, 40
  ret


global _start
_start:
  mov rax, 34
  push rax
  mov rax, 35
  push rax
  pop rax
  pop rbx
  add rax, rbx
  push rax
  pop rdi
  call puti
  mov rax, 33
  push rax
  mov rax, 1
  mov rdi, 1
  mov rsi, c0
  mov rdx, 1
  syscall
  mov rax, 33
  push rax
  mov rax, 1
  mov rdi, 1
  mov rsi, c0
  mov rdx, 1
  syscall
  mov rax, 10
  push rax
  mov rax, 1
  mov rdi, 1
  mov rsi, c1
  mov rdx, 1
  syscall
  mov rax, 0
  push rax
  mov rax, 60
  pop rdi
  syscall
segment .data:
c0: db 33
c1: db 10
