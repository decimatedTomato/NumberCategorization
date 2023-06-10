import AliquotSequence
import Prime
import Palindromic

class AnalysisSpecification:
    input: int | list[int] | range
    
    analyze_prime: bool = True
    analyze_aliquot: bool = True
    analyze_palindrome: bool = False

    def analyze(self, value):
        if self.analyze_prime:
            prime_property = Prime.priminess(value)
            match prime_property:
                case Prime.Priminess.ZERO:
                    pass
                case Prime.Priminess.PRIME_HIGHLY_COMPOSITE:
                    print(f"{value} is a prime and highly composite number ({len(Prime._prime_factorize(value)) + 1} factors)")
                case Prime.Priminess.HIGHLY_COMPOSITE:
                    print(f"{value} is a highly composite number ({len(Prime._prime_factorize(value)) + 1} factors)")
                case Prime.Priminess.COMPOSITE:
                    print(f"{value} is a composite number")
                case Prime.Priminess.PRIME:
                    print(f"{value} is a prime number")
                case Prime.Priminess.SEMPIPRIME:
                    print(f"{value} is a semiprime number {dict(Prime._prime_factorize(value))}")
            
        if self.analyze_aliquot:
            aliquot_property = AliquotSequence.aliquot_property(value)
            if aliquot_property != None:
                print(f"Aliquot sequence property of {value} is {aliquot_property}")
            aliquot_sequence = AliquotSequence.aliquot_sequence(value)[0]
            print(f"Aliquot sequence starting at {value} has length {len(aliquot_sequence)}:\n{aliquot_sequence}")

        if self.analyze_palindrome:
            is_palindromic = Palindromic.palindromic(value)
            if is_palindromic:
                print(f"{value} is palindromic")

    def report_results(self):
        if type(self.input) == range:
            for i in self.input:
                self.analyze(i)
        elif type(self.input) == int:
            self.analyze(self.input)
        
        

def main():
    anal_spec = AnalysisSpecification()
    print("Let's start analyzing numbers!")
    try:
        while True:
            user_input = input("\nNumber to analyze: ")
            if user_input in ["q", "quit", "exit"]:
                break
            elif user_input[:3] == "set":
                raise NotImplementedError #TODO allow configuation
            try:
                # handle list
                if "," in user_input:
                    anal_spec.input = [int(i) for i in user_input.split(",")]
                # handle range
                if ":" in user_input:
                    a, b, c = map(int, user_input.split(":")) #TODO issues
                    anal_spec.input = range(a, b, c)
                # handle int
                else:
                    anal_spec.input = int(user_input)
            except ValueError:
                print(f"<{user_input}> is not a number, try again?")
                continue
            anal_spec.report_results()
    except KeyboardInterrupt:
        pass
    print("Enough analyzing for now. Good bye :]")

if __name__ == "__main__":
    main()