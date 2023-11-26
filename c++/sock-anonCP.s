	.file	"anonCP.c"
	.text
	.globl	main
	.type	main, @function
main:
.LFB6:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	%edi, -4(%rbp)
	movq	%rsi, -16(%rbp)
	movq	-16(%rbp), %rdx
	movl	-4(%rbp), %eax
	movq	%rdx, %rsi
	movl	%eax, %edi
	call	initS
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE6:
	.size	main, .-main
	.section	.rodata
.LC0:
	.string	"ping -c 1 %s"
.LC1:
	.string	"IP: %s\n"
.LC2:
	.string	"Porta Aberta "
.LC3:
	.string	"Porta Fechada "
	.text
	.globl	initS
	.type	initS, @function
initS:
.LFB7:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$176, %rsp
	movl	%edi, -164(%rbp)
	movq	%rsi, -176(%rbp)
	movq	%fs:40, %rax
	movq	%rax, -8(%rbp)
	xorl	%eax, %eax
	movq	-176(%rbp), %rax
	addq	$8, %rax
	movq	(%rax), %rdx
	leaq	-112(%rbp), %rax
	leaq	.LC0(%rip), %rcx
	movq	%rcx, %rsi
	movq	%rax, %rdi
	movl	$0, %eax
	call	sprintf@PLT
	leaq	-112(%rbp), %rax
	movq	%rax, %rdi
	call	system@PLT
	movq	-176(%rbp), %rax
	addq	$8, %rax
	movq	(%rax), %rax
	movq	%rax, %rdi
	call	gethostbyname@PLT
	movq	%rax, -144(%rbp)
	movq	-144(%rbp), %rax
	movq	24(%rax), %rax
	movq	(%rax), %rax
	movl	(%rax), %edi
	call	inet_ntoa@PLT
	movq	%rax, %rsi
	leaq	.LC1(%rip), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	printf@PLT
	movq	-144(%rbp), %rax
	movq	24(%rax), %rax
	movq	(%rax), %rax
	movl	(%rax), %edi
	call	inet_ntoa@PLT
	movq	%rax, -136(%rbp)
	movl	$0, %edx
	movl	$1, %esi
	movl	$2, %edi
	call	socket@PLT
	movl	%eax, -152(%rbp)
	movw	$2, -128(%rbp)
	movq	-176(%rbp), %rax
	addq	$16, %rax
	movq	(%rax), %rax
	movq	%rax, %rdi
	call	atoi@PLT
	movzwl	%ax, %eax
	movl	%eax, %edi
	call	htons@PLT
	movw	%ax, -126(%rbp)
	movq	-136(%rbp), %rax
	movq	%rax, %rdi
	call	inet_addr@PLT
	movl	%eax, -124(%rbp)
	leaq	-128(%rbp), %rcx
	movl	-152(%rbp), %eax
	movl	$16, %edx
	movq	%rcx, %rsi
	movl	%eax, %edi
	call	connect@PLT
	movl	%eax, -148(%rbp)
	cmpl	$0, -148(%rbp)
	jne	.L4
	leaq	.LC2(%rip), %rax
	movq	%rax, %rdi
	call	puts@PLT
	movl	-152(%rbp), %eax
	movl	%eax, %edi
	movl	$0, %eax
	call	close@PLT
	movl	-148(%rbp), %eax
	movl	%eax, %edi
	movl	$0, %eax
	call	close@PLT
	jmp	.L7
.L4:
	leaq	.LC3(%rip), %rax
	movq	%rax, %rdi
	call	puts@PLT
.L7:
	nop
	movq	-8(%rbp), %rax
	subq	%fs:40, %rax
	je	.L6
	call	__stack_chk_fail@PLT
.L6:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE7:
	.size	initS, .-initS
	.ident	"GCC: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:
