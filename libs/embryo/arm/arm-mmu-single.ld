/* 0 - 0000ffff is left unmapped to guard against null pointer derefs */
__ram_map_start__       = 0x00010000;
/* FCSE cuts virtual address space into 32MB chunks, we might use this later
 * so for now all the RAM mappings are expected to fit in the first 32MB */
__ram_map_end__         = 0x02000000;
/* ROM gets stuffed up near the top out of the way */
__rom_map_start__       = 0xf0000000;
/* initrd goes at the top too */
__initrd_map_start__    = 0xf8000000;
/* fixed address mappings go right at the top of the address space just below
 * the vectors */
__page_tbl_start__      = 0xffb00000; /* 4mb, enough to map 4gb */
__page_tbl_end__        = 0xfff00000;
__page_dir_virt__       = 0xfff00000; /* 16kb */
__dbg_serial_virt__     = 0xfff10000; /* 4kb */
__bootdata_virt__       = 0xfff20000; /* 4kb */
__exc_stack_start__     = 0xfff30000; /* 4kb, shared for all modes */
__exc_stack_end__       = 0xfff31000;
__vectors__             = 0xffff0000; /* 4kb */
