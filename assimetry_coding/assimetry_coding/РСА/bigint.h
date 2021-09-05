#ifndef BIGINT_H
#define BIGINT_H
	#include <iostream>
	
	class bigint
	{
	private:
		bool is_positive;
		char *data;
		bool is_ok(void);
		static unsigned char std_len;
		friend int try_fix_from_plus(bigint& value);
		friend int try_fix_from_minus(bigint& value);
		bool is_less_than_zero(void);
	public:
		bigint(void);
		bigint(std::string value);
		bigint(const bigint &other);
		~bigint(void);
		bigint operator- (void);
		bigint operator= (bigint right);
		bigint operator+ (bigint right);
		bigint operator- (bigint right);
		bigint operator/ (bigint right);
		bigint operator* (bigint right);
		bigint operator^ (bigint right);
		bigint operator% (bigint right);
		bool operator> (bigint right);
		bool operator< (bigint right);
		bool operator== (bigint right);
		bool operator!= (bigint right);
		bool operator>= (bigint right);
		bool operator<= (bigint right);
		friend std::ostream& operator<< (std::ostream &out, bigint value);
		friend std::istream& operator>> (std::istream &in, bigint &value);
	};
#endif /*BIGINT_H*/
