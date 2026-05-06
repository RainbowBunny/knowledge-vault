
## Compilation System

- **Preprocessing Phase**:
- **Compilation Phase**:
- **Assembly Phase**:
- **Linking Phase**:

> [!remark] Why should we understand how compilation system work
> - **Optimizing program performance**
> - **Understanding link-time errors**
> - **Avoiding security holes**

## Hardware Organization

> [!definition] Important Components
> - **Buses**: Carrying data (electrical conduits) from component to component.
> - **I/O Devices**: Connection to external world.
> - **Main Memory**: Temporary storage device that holds both a program and data it manipulates while the processor is executing the program.
> - **Processor**: An engine that executes the instruction.

## Storage Device

> [!remark]
> `Regs > L1 Cache > L2 Cache > L3 Cache > Main Memory (DRAM) > Local secondary storages (local disks) > Remote secondary storage (distributed file systems, Web servers)`

## Abstraction

```
I/O Devices = Files
Virtual Memory = Main Memory + I/O Devices
Processor = Instruction Set Architecture
Processes = Processor + Main Memory + I/O Devices
Virtual Machine = Operating System + Processor + Main Memory + I/O Devices
```

