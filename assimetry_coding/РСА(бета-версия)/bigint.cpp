#include <iostream>
#include "bigint.h"

unsigned char bigint::std_len = 100;

bigint::bigint(void)
{
	this -> is_positive = true;
	this -> data = new char [bigint::std_len];
	for (int i = 0; i < bigint::std_len; ++i)
	{
		this -> data[i] = 0;
	};
};

bigint::~bigint(void)
{
	delete [] this -> data;
};

bigint::bigint(std::string value)
{
	this -> is_positive = true;
	if (value[0] == '-')
	{
		value.erase(value.begin());
		this -> is_positive = false;
	};
	this -> data = new char [bigint::std_len];
	for (int i = value.length() - 1; i >= 0; --i)
	{
		this -> data[value.length() - 1 - i] = value[i] - '0';
	};
	for (int i = value.length(); i < bigint::std_len; ++i)
	{
		this -> data[i] = 0;
	};
};

std::ostream& operator<< (std::ostream &out, bigint value)
{
	out << ( (value.is_positive) ? ("") : ("-") );
	bool has_lead_nulls = true;
	for (int i = bigint::std_len - 1; i >= 0; --i)
	{
		if (value.data[i] != 0)
		{
			has_lead_nulls = false;
		};
		if (has_lead_nulls)
		{
			continue;
		};
		out << (int)value.data[i];
	};
	if (has_lead_nulls)
	{
		out << 0;
	};
	return out; 
};

std::istream& operator>> (std::istream &in, bigint &value)
{
	std::string new_value;
	in >> new_value;
	value = bigint(new_value);
	return in;
};

bigint bigint::operator= (bigint right)
{
	this -> is_positive = right.is_positive;
	delete [] this -> data;
	this -> data = new char [bigint::std_len];
	for (int i = 0; i < bigint::std_len; ++i)
	{
		this -> data[i] = right.data[i];
	};
	return *this;
};

bigint::bigint(const bigint &other)
{
	this -> data = new char [bigint::std_len];
	this -> is_positive = other.is_positive;
	for (int i = 0; i < this -> bigint::std_len; ++i)
	{
		this -> data[i] = other.data[i];
	};
};

bigint bigint::operator+ (bigint right)
{
	bigint tmp;
	if (this -> is_positive == right.is_positive)
	{
			for (int i = 0; i < bigint::std_len; ++i)
			{
				tmp.data[i] = this -> data[i] + right.data[i];
			};
			while ( !tmp.is_ok() )
			{
				try_fix_from_plus(tmp);
			};
			tmp.is_positive = this -> is_positive;
	}
	else
	{
		if (*this > right)
		{
			right.is_positive = true;
			tmp = *this - right;
		}
		else
		{
			bigint nthis = *this;
			nthis.is_positive = true;
			tmp = right - nthis;
		};
	};
	return tmp;
};

bool bigint::operator> (bigint right)
{
	if ((this -> is_positive) && (right.is_positive))
	{
		for (int i = bigint::std_len - 1; i >= 0; --i)
		{
			if (this -> data[i] != right.data[i])
			{
				return this -> data[i] >  right.data[i];
			};
		};
		return false;
	}
	else
	
	if ((!this -> is_positive)&&(right.is_positive))
	{
		return false;
	}
	else

	if ((this -> is_positive)&&(!right.is_positive))
	{
		return true;
	}
	else
	
	if ((!this -> is_positive)&&(!right.is_positive))
	{
		for (int i = bigint::std_len - 1; i >= 0; --i)
		{
			if (this -> data[i] != right.data[i])
			{
				return this -> data[i] < right.data[i];
			};
		};
		return false;		
	};
	return !(true) && !(false); 
};

bool bigint::operator< (bigint right)
{
	if ((this -> is_positive) && (right.is_positive))
	{
		for (int i = bigint::std_len - 1; i >= 0; --i)
		{
			if (this -> data[i] != right.data[i])
			{
				return this -> data[i] <  right.data[i];
			};
		};
		return false;
	}
	else
	
	if ((!this -> is_positive)&&(right.is_positive))
	{
		return true;
	}
	else

	if ((this -> is_positive)&&(!right.is_positive))
	{
		return false;
	}
	else
	
	if ((!this -> is_positive)&&(!right.is_positive))
	{
		for (int i = bigint::std_len - 1; i >= 0; --i)
		{
			if (this -> data[i] != right.data[i])
			{
				return this -> data[i] >  right.data[i];
			};
		};
		return false;		
	};
	return !(true) && !(false); 
};

bool bigint::operator== (bigint right)
{
	if (this -> is_positive != right.is_positive)
	{
		return false;
	};
	
	for (int i = bigint::std_len - 1; i >= 0; --i)
	{
		if (this -> data[i] != right.data[i])
		{
			return false;
		};
	};
	return true;
};

bool bigint::operator!= (bigint right)
{
	return !(*this == right);
};

bool bigint::operator>= (bigint right)
{
	return (*this > right) || (*this == right);
};

bool bigint::operator<= (bigint right)
{
	return (*this < right) || (*this == right); 
};


bigint bigint::operator- (bigint right)
{
	bigint tmp;
	if ((this -> is_positive) == (right.is_positive))
	{
		if (right <= *this)
		{
			if (this -> is_positive)
			{
				for (int i = 0; i < bigint::std_len; ++i)
				{
					tmp.data[i] = this -> data[i] - right.data[i];
				};
				while (!tmp.is_ok())
				{
					try_fix_from_minus(tmp);
				};
			}
			else
			{
				right.is_positive = true;
				bigint nthis = *this;
				nthis.is_positive = true;
				tmp = nthis - right;
				tmp.is_positive = true;
			};	
		}
		else
		{
			if (this -> is_positive)
			{
				right.is_positive = true;
				bigint nthis = *this;
				nthis.is_positive = true;
				tmp = right - nthis;
				tmp.is_positive = false;
			}
			else
			
			{
				right.is_positive = true;
				bigint nthis = *this;
				nthis.is_positive = true;
				tmp = right - nthis;
				tmp.is_positive = false;
			};
		};
	}
	else	
	{
		bool positive = this -> is_positive;
		bigint nthis = *this;
		nthis.is_positive = true;
		right.is_positive = true;
		tmp = nthis + right;
		tmp.is_positive = positive;
	};
	return tmp;
};

bigint bigint::operator/ (bigint right)
{
	bigint sum;
	bigint tmp = *this;
	while (tmp > bigint("0"))
	{
		
	};
	return sum;
};

bigint bigint::operator- (void)
{
	this -> is_positive = !this -> is_positive;
	return *this;
};

bigint bigint::operator* (bigint right)
{
	bigint tmp;
	if (right.is_positive != this -> is_positive)
	{
		tmp.is_positive = false;
	};
	right.is_positive = true;
	this -> is_positive = true;
	for (bigint i; i < right; i = i + bigint("1"))
	{
		tmp = tmp + *this;
	};
	return tmp;
};

bigint bigint::operator^ (bigint right)
{
	return bigint("0");
};

bigint bigint::operator% (bigint right)
{
	return bigint("0");
};

bool bigint::is_ok(void)
{
	for (int i = 0; i < bigint::std_len; ++i)
	{
		if ((this -> data[i] < 0) || (this -> data[i] > 9))
		{
			return false;
		};
	};
	return true;
};

int try_fix_from_plus(bigint& value)
{	
	for (int i = 0; i < bigint::std_len; ++i)
	{
		value.data[i + 1] += value.data[i] / 10;
		value.data[i] %= 10;
	};	
	return 0;
};

int try_fix_from_minus(bigint& value)
{
	for (int i = 0; i < bigint::std_len - 1; ++i)
	{
		if ((value.data[i] < 0))
		{
			value.data[i] += 10;
			value.data[i + 1] -= 1;
		};
	};
	return 0;
};

bool bigint::is_less_than_zero(void)
{
	for (int i = 0; i < bigint::std_len; ++i)
	{
		if (this -> data[i] > 0)
		{
			return false;
		};
	};
	return true;
};
