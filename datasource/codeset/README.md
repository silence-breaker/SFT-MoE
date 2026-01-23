# srsRAN Project - 代码库文档

## 项目概述

srsRAN Project 是一个开源的5G NR (New Radio) 无线接入网络实现项目，由 Software Radio Systems Limited 开发和维护。该项目实现了完整的 gNB (5G 基站) 协议栈，符合 3GPP 5G NR 标准规范。

本代码库位于 `lib/` 目录下，包含了 srsRAN gNB 的核心库实现。

---

## 目录结构与模块说明

### 1. CU-CP (Central Unit - Control Plane) 模块
**路径**: `cu_cp/`

CU-CP 是 5G 基站的中央控制面单元，负责处理无线资源控制 (RRC) 和非接入层 (NAS) 信令。

#### 核心文件说明：
| 文件名 | 功能描述 |
|--------|----------|
| `cu_cp_impl.cpp/h` | CU-CP 主实现类，协调各子模块工作 |
| `cu_cp_factory.cpp` | CU-CP 实例工厂，创建 CU-CP 对象 |
| `cu_configurator_impl.cpp/h` | CU 配置器，处理配置更新 |
| `ngap_repository.cpp/h` | NGAP 连接仓库，管理与 AMF 的连接 |
| `o_cu_cp_impl.cpp/h` | O-RAN 兼容的 CU-CP 实现 |

#### 子模块：
- **adapters/**: 适配器模式实现，连接各协议层
- **ue_manager/**: UE (用户设备) 上下文管理
- **du_processor/**: DU 处理器，管理与 DU 的交互
- **cu_up_processor/**: CU-UP 处理器
- **mobility_manager/**: 移动性管理，处理切换
- **paging/**: 寻呼处理
- **routines/**: 异步任务和例程
- **task_schedulers/**: 任务调度器
- **ue_security_manager/**: UE 安全管理
- **up_resource_manager/**: 用户面资源管理
- **cell_meas_manager/**: 小区测量管理
- **metrics_handler/**: 指标收集处理

---

### 2. CU-UP (Central Unit - User Plane) 模块
**路径**: `cu_up/`

CU-UP 是 5G 基站的中央用户面单元，负责处理用户数据传输。

#### 核心文件说明：
| 文件名 | 功能描述 |
|--------|----------|
| `cu_up_impl.cpp/h` | CU-UP 主实现类 |
| `cu_up_factory.cpp` | CU-UP 实例工厂 |
| `cu_up_manager_impl.cpp/h` | CU-UP 管理器实现 |
| `ue_manager.cpp/h` | UE 上下文管理 |
| `pdu_session_manager_impl.cpp/h` | PDU 会话管理器 |
| `ngu_session_manager_impl.cpp/h` | NG-U 会话管理 |
| `drb_context.h` | 数据无线承载 (DRB) 上下文 |
| `qos_flow_context.h` | QoS 流上下文 |
| `ue_context.h` | UE 上下文定义 |
| `o_cu_up_impl.cpp/h` | O-RAN 兼容的 CU-UP 实现 |

---

### 3. DU (Distributed Unit) 模块
**路径**: `du/`

DU 是 5G 基站的分布式单元，负责实时的无线处理。

#### 核心文件说明：
| 文件名 | 功能描述 |
|--------|----------|
| `o_du_impl.cpp/h` | O-RAN DU 主实现 |
| `o_du_factory.cpp` | O-DU 工厂 |
| `du_cell_config_validation.cpp` | 小区配置验证 |
| `du_update_config_helpers.cpp` | 配置更新助手 |

#### 子模块：
- **du_high/**: DU-High 层，处理 MAC/RLC 层功能
- **du_low/**: DU-Low 层，处理物理层相关功能

---

### 4. NGAP (NG Application Protocol) 模块
**路径**: `ngap/`

NGAP 是 gNB 与 5G 核心网 (AMF) 之间的控制面协议。

#### 核心文件说明：
| 文件名 | 功能描述 |
|--------|----------|
| `ngap_impl.cpp/h` | NGAP 协议主实现 |
| `ngap_factory.cpp` | NGAP 实例工厂 |
| `ngap_connection_handler.cpp/h` | NGAP 连接处理 |
| `ngap_asn1_packer.cpp/h` | ASN.1 消息打包/解包 |
| `ngap_asn1_utils.cpp/h` | ASN.1 工具函数 |
| `ngap_asn1_helpers.h` | ASN.1 转换助手 |
| `ngap_asn1_converters.h` | 数据类型转换器 |
| `log_helpers.cpp/h` | 日志助手 |

#### 子模块：
- **procedures/**: NGAP 过程实现 (NG Setup, UE Context Setup 等)
- **ue_context/**: NGAP UE 上下文管理
- **metrics/**: NGAP 指标收集
- **gateways/**: N2 网关实现

---

### 5. F1AP (F1 Application Protocol) 模块
**路径**: `f1ap/`

F1AP 是 CU 与 DU 之间的接口协议。

#### 核心文件说明：
| 文件名 | 功能描述 |
|--------|----------|
| `f1ap_asn1_packer.cpp/h` | F1AP ASN.1 消息处理 |
| `f1ap_common_messages.cpp/h` | F1AP 公共消息 |
| `asn1_helpers.cpp/h` | ASN.1 辅助函数 |
| `log_helpers.cpp/h` | 日志辅助函数 |
| `proc_logger.h` | 过程日志记录器 |

#### 子模块：
- **cu_cp/**: CU-CP 侧 F1AP 实现
- **du/**: DU 侧 F1AP 实现
- **gateways/**: F1 网关

---

### 6. E1AP (E1 Application Protocol) 模块
**路径**: `e1ap/`

E1AP 是 CU-CP 与 CU-UP 之间的接口协议。

#### 子模块：
- **common/**: 公共组件
- **cu_cp/**: CU-CP 侧 E1AP 实现
- **cu_up/**: CU-UP 侧 E1AP 实现
- **gateways/**: E1 网关

---

### 7. MAC (Medium Access Control) 层模块
**路径**: `mac/`

MAC 层负责无线资源的调度和管理。

#### 核心文件说明：
| 文件名 | 功能描述 |
|--------|----------|
| `mac_impl.cpp/h` | MAC 层主实现 |
| `mac_factory.cpp` | MAC 实例工厂 |
| `rnti_manager.h` | RNTI (无线网络临时标识) 管理 |

#### 子模块：
- **mac_ctrl/**: MAC 控制器，UE 配置管理
- **mac_dl/**: MAC 下行处理，PDU 生成
- **mac_ul/**: MAC 上行处理，PDU 解析
- **mac_sched/**: MAC 调度器接口
- **config/**: MAC 配置

---

### 8. RLC (Radio Link Control) 层模块
**路径**: `rlc/`

RLC 层提供可靠/非可靠的数据传输服务。

#### 核心文件说明：
| 文件名 | 功能描述 |
|--------|----------|
| `rlc_factory.cpp` | RLC 实体工厂 |
| `rlc_am_entity.h` | RLC AM (确认模式) 实体 |
| `rlc_um_entity.h` | RLC UM (非确认模式) 实体 |
| `rlc_tm_entity.h` | RLC TM (透明模式) 实体 |
| `rlc_rx_am_entity.cpp/h` | AM 模式接收实体 |
| `rlc_tx_am_entity.cpp/h` | AM 模式发送实体 |
| `rlc_rx_um_entity.cpp/h` | UM 模式接收实体 |
| `rlc_tx_um_entity.cpp/h` | UM 模式发送实体 |
| `rlc_am_pdu.cpp/h` | AM PDU 处理 |
| `rlc_um_pdu.h` | UM PDU 处理 |
| `rlc_bearer_logger.h` | 承载日志记录 |
| `rlc_bearer_metrics_collector.cpp/h` | 承载指标收集 |

---

### 9. PDCP (Packet Data Convergence Protocol) 层模块
**路径**: `pdcp/`

PDCP 层负责数据压缩、加密和完整性保护。

#### 核心文件说明：
| 文件名 | 功能描述 |
|--------|----------|
| `pdcp_factory.cpp` | PDCP 实体工厂 |
| `pdcp_entity_impl.h` | PDCP 实体实现 |
| `pdcp_entity_tx.cpp/h` | PDCP 发送处理 |
| `pdcp_entity_rx.cpp/h` | PDCP 接收处理 |
| `pdcp_pdu.cpp/h` | PDCP PDU 处理 |
| `pdcp_tx_window.cpp/h` | 发送窗口管理 |
| `pdcp_sn.h` | 序列号处理 |
| `pdcp_metrics_aggregator.cpp/h` | 指标聚合 |
| `pdcp_crypto_token.h` | 加密令牌 |

---

### 10. Scheduler (调度器) 模块
**路径**: `scheduler/`

调度器负责无线资源的分配和调度决策。

#### 核心文件说明：
| 文件名 | 功能描述 |
|--------|----------|
| `scheduler_impl.cpp/h` | 调度器主实现 |
| `scheduler_factory.cpp` | 调度器工厂 |
| `cell_scheduler.cpp/h` | 小区级调度器 |

#### 子模块：
- **ue_scheduling/**: UE 级调度
- **cell/**: 小区资源管理
- **pdcch_scheduling/**: PDCCH 调度
- **pucch_scheduling/**: PUCCH 调度
- **common_scheduling/**: 通用调度逻辑
- **policy/**: 调度策略 (RR, PF 等)
- **config/**: 调度器配置
- **logging/**: 调度器日志
- **slicing/**: 网络切片支持
- **support/**: 支持函数

---

### 11. RRC (Radio Resource Control) 模块
**路径**: `rrc/`

RRC 层负责无线资源控制和 UE 状态管理。

#### 核心文件说明：
| 文件名 | 功能描述 |
|--------|----------|
| `rrc_du_impl.cpp/h` | RRC DU 实现 |
| `rrc_du_factory.cpp` | RRC DU 工厂 |

#### 子模块：
- **ue/**: UE 相关 RRC 过程
- **metrics/**: RRC 指标

---

### 12. SDAP (Service Data Adaptation Protocol) 层模块
**路径**: `sdap/`

SDAP 层负责 QoS 流与数据无线承载 (DRB) 之间的映射。

#### 核心文件说明：
| 文件名 | 功能描述 |
|--------|----------|
| `sdap_factory.cpp` | SDAP 实体工厂 |
| `sdap_entity_impl.h` | SDAP 实体实现 |
| `sdap_entity_tx_impl.h` | SDAP 发送处理 |
| `sdap_entity_rx_impl.h` | SDAP 接收处理 |
| `sdap_session_logger.h` | 会话日志 |

---

### 13. GTP-U (GPRS Tunnelling Protocol - User Plane) 模块
**路径**: `gtpu/`

GTP-U 负责用户面数据在 gNB 与核心网之间的隧道传输。

#### 核心文件说明：
| 文件名 | 功能描述 |
|--------|----------|
| `gtpu_pdu.cpp/h` | GTP-U PDU 处理 |
| `gtpu_demux_impl.cpp/h` | GTP-U 解复用器 |
| `gtpu_demux_factory.cpp` | 解复用器工厂 |
| `gtpu_echo_impl.h` | GTP-U Echo 处理 |
| `gtpu_gateway.cpp` | GTP-U 网关 |
| `gtpu_teid_pool_impl.h` | TEID 池管理 |
| `gtpu_tunnel_*.h/cpp` | GTP-U 隧道实现 |

---

### 14. Security (安全) 模块
**路径**: `security/`

安全模块实现 5G NR 的加密和完整性保护算法。

#### 核心文件说明：
| 文件名 | 功能描述 |
|--------|----------|
| `security.cpp` | 安全功能主实现 |
| `security_engine_impl.cpp/h` | 安全引擎 |
| `ciphering_engine_nea1.cpp/h` | NEA1 (SNOW 3G) 加密算法 |
| `ciphering_engine_nea2.cpp/h` | NEA2 (AES) 加密算法 |
| `ciphering_engine_nea3.cpp/h` | NEA3 (ZUC) 加密算法 |
| `integrity_engine_*.cpp/h` | 完整性保护算法 (NIA1/2/3) |
| `s3g.cpp/h` | SNOW 3G 算法实现 |
| `zuc.cpp` | ZUC 算法实现 |

---

### 15. PHY (Physical Layer) 物理层模块
**路径**: `phy/`

物理层负责信号的调制解调和传输。

#### 子模块：
- **upper/**: 上层物理处理
- **lower/**: 下层物理处理
- **generic_functions/**: 通用物理层函数
- **support/**: 物理层支持函数
- **metrics/**: 物理层指标

---

### 16. RAN (Radio Access Network) 模块
**路径**: `ran/`

RAN 模块提供无线接入网络的通用功能和配置。

#### 子目录：
- **ssb/**: SSB (同步信号块) 相关
- **prach/**: PRACH (随机接入) 配置
- **pdcch/**: PDCCH 相关
- **pdsch/**: PDSCH 相关
- **pusch/**: PUSCH 相关
- **pucch/**: PUCCH 相关
- **sch/**: 传输块大小计算
- **csi_rs/**: CSI-RS 相关
- **srs/**: SRS 配置
- **qos/**: QoS 映射
- **cause/**: 原因码转换

---

### 17. Support (支持) 模块
**路径**: `support/`

提供通用支持功能和基础设施。

#### 核心文件说明：
| 文件名 | 功能描述 |
|--------|----------|
| `byte_buffer.cpp` | 字节缓冲区实现 |
| `timers.cpp` | 定时器管理 |
| `signal_handling.cpp` | 信号处理 |
| `backtrace.cpp` | 堆栈追踪 |
| `config_yaml.cpp` | YAML 配置解析 |

#### 子模块：
- **executors/**: 任务执行器框架
- **network/**: 网络工具
- **tracing/**: 追踪功能
- **synchronization/**: 同步原语

---

### 18. FAPI (Fronthaul API) 模块
**路径**: `fapi/`

FAPI 是 MAC 与物理层之间的接口。

#### 核心功能：
- 配置消息网关
- 消息验证
- 消息缓冲

---

### 19. E2 (E2 Interface) 模块
**路径**: `e2/`

E2 接口用于 O-RAN 近实时 RIC (RAN Intelligent Controller)。

#### 子模块：
- **common/**: 公共组件
- **e2sm/**: E2 服务模型
- **procedures/**: E2 过程
- **gateways/**: E2 网关

---

### 20. ASN.1 模块
**路径**: `asn1/`

ASN.1 编解码支持所有协议层。

#### 子模块：
- **e1ap/**: E1AP ASN.1
- **e2ap/**: E2AP ASN.1
- **f1ap/**: F1AP ASN.1
- **ngap/**: NGAP ASN.1
- **rrc_nr/**: RRC NR ASN.1
- **e2sm/**: E2 服务模型 ASN.1

---

## 协议栈架构图

```
                    +------------------+
                    |     5G Core      |
                    |      (AMF)       |
                    +--------+---------+
                             | N2 (NGAP)
                    +--------+---------+
                    |                  |
                    |     CU-CP        |
                    |  (RRC, NGAP)     |
                    +--------+---------+
                   /         |          \
            E1AP  /          |           \  F1-C (F1AP)
                 /           |            \
    +-----------+    +-------+-------+    +-----------+
    |  CU-UP    |    |               |    |    DU     |
    | (SDAP,    |<-->|  F1-U (GTP-U) |<-->| (MAC,RLC) |
    |  PDCP)    |    |               |    |           |
    +-----------+    +---------------+    +-----------+
                                                |
                                          +-----+-----+
                                          |    PHY    |
                                          +-----------+
                                                |
                                          +-----+-----+
                                          |    RF     |
                                          +-----------+
```

---

## 主要技术特点

1. **模块化设计**: 采用清晰的层次化架构，各模块职责分明
2. **O-RAN 兼容**: 支持 O-RAN 定义的接口和分离架构
3. **异步处理**: 大量使用 async_task 进行异步操作
4. **工厂模式**: 各模块使用工厂模式创建实例
5. **适配器模式**: 使用适配器连接不同协议层
6. **指标收集**: 内置全面的性能指标收集机制
7. **可配置性**: 支持丰富的运行时配置选项

---

## 许可证

本代码采用 GNU Affero General Public License (AGPL) v3.0 或更高版本许可。

---

## 参考资料

- [3GPP 5G NR 规范](https://www.3gpp.org/dynareport?code=38-series.htm)
- [O-RAN 联盟规范](https://www.o-ran.org/specifications)
- [srsRAN 官方文档](https://docs.srsran.com/)

---

*文档生成时间: 2026年1月20日*
