This is a patch set for qemu generated by `git format-patch`. These patches
are required to use debug_lockstep to debug the LEG processor, since they
add additional communication functionality between qemu and GDB. This allows us
to

 - get an accurate instruction count
 - dump qemu's coprocessor registers
 - check if interrupts (IRQ or FIQ) are pending
 - log all IO accesses so that we read the same values in ModelSim
 - not kill qemu when GDB tries to read bad addresses during `stepi`

To apply the patches, you should clone qemu in git, and then run
```
git checkout -b leg-additions v2.4.0
git am path/to/LEG/qemu_patches/*
```

You can then `configure` and `make` qemu as normal.

To (re)generate the patches, in your qemu directory run
```
git format-patch v2.4.0 -o path/to/LEG/qemu_patches
```
