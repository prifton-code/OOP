class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.is_on = False
        self.battery = 100
    
    def power_on(self):
        if self.battery > 0:
            self.is_on = True
            return f"{self.brand} {self.model} is now on!"
        return "Battery is dead. Please charge."
    
    def power_off(self):
        self.is_on = False
        return "Phone is now off."
    
    def use_battery(self, amount):
        self.battery = max(0, self.battery - amount)
        if self.battery == 0:
            self.is_on = False
        return f"Battery: {self.battery}%"
    
    def charge(self):
        self.battery = 100
        return "Phone is fully charged!"
    
    def __str__(self):
        status = "on" if self.is_on else "off"
        return f"{self.brand} {self.model} ({self.storage}GB) - Battery: {self.battery}% - Status: {status}"


# Simple inheritance example
class PremiumPhone(Smartphone):
    def __init__(self, brand, model, storage, has_5g=True):
        super().__init__(brand, model, storage)
        self.has_5g = has_5g
    
    def use_5g(self):
        if self.has_5g:
            return "Using 5G network!"
        return "5G not available"
    
    # Override the use_battery method for faster drain
    def use_battery(self, amount):
        # Premium phones use more battery
        extra_drain = amount * 0.5  # 50% more battery usage
        return super().use_battery(amount + extra_drain)


# Demonstration
if __name__ == "__main__":
    print("=== Regular Phone ===")
    basic_phone = Smartphone("Basic", "A10", 64)
    print(basic_phone)
    print(basic_phone.power_on())
    print(basic_phone.use_battery(20))
    print(basic_phone.charge())
    
    print("\n=== Premium Phone ===")
    premium_phone = PremiumPhone("Premium", "X5", 256)
    print(premium_phone)
    print(premium_phone.power_on())
    print(premium_phone.use_5g())
    print(premium_phone.use_battery(20))  # Will drain more battery