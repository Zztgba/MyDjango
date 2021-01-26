ATOMIC_REQUESTS: True or False

    True 开启每个view都会单独事务提交

AUTOCOMMIT: True or False
    
    自动开启Django的事务管理。关闭后将自己控制事务提交
    
CONN_MAX_AGE: Integer

    连接生命周期，秒为单位。默认0，每个请求结束关闭连接；设置None时，连接永不关闭
    
