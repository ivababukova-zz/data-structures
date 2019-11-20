# Design an API that supports the following function calls:

# public class ServiceManager {

# 	public void addService(String service) {
# 		// todo
# 	}

# 	public void addServiceCall(String service, long time, String payload) {
# 		// todo
# 	}

# 	public List<String> getAllServiceCallsBetweenTimes(long time1, long time2) {
# 		// todo
# 	}
# }

# Example:

# ServiceManager m = new ServiceManager();
# m.addService("A");
# m.addService("B");
# m.addServiceCall("A", 1, "abc");
# m.addServiceCall("A", 5, "abec");
# m.addServiceCall("B", 3, "ac");
# m.getAllServiceCallsBetweenTimes(1, 4); // ["abc", "ac"]
# Follow-up:
# What if you also had to filter by service?

class ServiceManager:

    def __init__(self):
        pass

    def add_service(service_name):
        pass

    def add_service_call(service_name, t, payload):
        pass

    def get_all_service_calls_between_times(t1, t2):
        pass